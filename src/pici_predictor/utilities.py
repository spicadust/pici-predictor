def parse_fasta_file(out_dir, df, id_col, seq_col):
    with open(out_dir, "w") as f:
        for idx, row in df.iterrows():
            f.write(f">{row[id_col]}\n")
            f.write(f"{row[seq_col]}\n")
    return out_dir


def parse_gff(gff_dir, out_dir):
    import pandas as pd

    records = []
    with open(gff_dir) as f:
        for line in f:
            if line.startswith("#"):
                continue
            parts = line.strip().split("\t")
            if len(parts) < 9 or parts[2] != "CDS":
                continue
            contig = parts[0]
            start = int(parts[3])
            end = int(parts[4])
            strand = parts[6]
            attributes = parts[8]
            # Try to extract protein_id or ID
            protein_id = None
            for attr in attributes.split(";"):
                if attr.startswith("protein_id="):
                    protein_id = attr.split("=")[1]
                    break
                elif attr.startswith("ID="):
                    protein_id = attr.split("=")[1]
            if protein_id:
                records.append(
                    {
                        "id": protein_id,
                        "contig": contig,
                        "start": start,
                        "end": end,
                        "strand": strand,
                    }
                )
    gff_df = (
        pd.DataFrame(records).sort_values(["contig", "start"]).reset_index(drop=True)
    )
    gff_df.to_csv(out_dir, index=False)
    print(f"gff_df.csv saved to {out_dir}")
    return gff_df


def feature_generation(fasta_dir, out_dir):
    import pandas as pd
    from tqdm import tqdm
    from Bio.SeqIO.FastaIO import SimpleFastaParser
    from pici_predictor.feature_generation import seq2features, create_genomic_features
    import warnings
    from Bio import BiopythonDeprecationWarning

    warnings.filterwarnings("ignore", category=BiopythonDeprecationWarning)

    def load_sequences(fasta_file):
        # Count lines to estimate number of sequences (optional, for better progress bar)
        with open(fasta_file, "r") as f:
            n_seqs = sum(1 for line in f if line.startswith(">"))

        with open(fasta_file, "r") as f:
            entries = [
                (name.split()[0], seq)
                for name, seq in tqdm(
                    SimpleFastaParser(f), total=n_seqs, desc="Loading sequences"
                )
            ]
        return entries

    def generate_features(entries, is_dna=False, chunk_size=None):
        if chunk_size is None:
            # Original behavior
            if is_dna:
                features_df = create_genomic_features(
                    "your_dna.fasta", file_format="fasta"
                )
            else:
                features_df = seq2features(entries, min_length=10, scaling=True)
            return features_df
        else:
            features_list = []
            for i in tqdm(
                range(0, len(entries), chunk_size), desc="Feature extraction"
            ):
                chunk = entries[i : i + chunk_size]
                features_chunk = seq2features(chunk, min_length=10, scaling=True)
                features_list.append(features_chunk)
            return pd.concat(features_list)

    # Load sequences
    entries = load_sequences(fasta_dir)

    # Generate features
    features_df = generate_features(entries)
    features_df = features_df.reset_index().rename(columns={"index": "id"})
    features_df = features_df.drop(columns=["md5"])
    # print(features_df.columns)

    # Save results
    features_df.to_parquet(out_dir)
    print(f"Features saved to {out_dir}")

    return features_df


def predict_function(feature_df, out_dir, model_path):
    import joblib
    import pandas as pd
    from pici_predictor.phrog_function import function_names_formatted

    function_list = [name for name in function_names_formatted if name != "no_hit"]
    predicted_probs = pd.DataFrame({"id": feature_df["id"]})

    for function_name in function_list:
        model_bundle = joblib.load(f"{model_path}/{function_name}_predictor.joblib")
        model = model_bundle["model"]
        scaler = model_bundle.get("scaler", None)
        feature_cols = model_bundle["feature_cols"]
        features = feature_df[feature_cols]

        # Apply scaler if present
        if scaler is not None:
            features = scaler.transform(features.values)
        else:
            features = features.values

        probs = model.predict_proba(features)[:, 1]
        predicted_probs[function_name] = probs

    predicted_probs.to_csv(out_dir, index=False)
    print(f"predicted_prob.csv saved to {out_dir}")
    return predicted_probs


def assign_functions(
    predicted_probs,
    threshold_dict,
    mu_neg_dict,
    sigma_neg_dict,
    function_to_num,
    out_dir,
):
    from pici_predictor.phrog_function import function_names_formatted
    import numpy as np

    function_list = [name for name in function_names_formatted if name != "no_hit"]

    def assign_function_row(row):
        above = []
        z_scores = []
        for fn in function_list:
            prob = row[fn]
            if prob >= threshold_dict[fn]:
                above.append(fn)
                z = (prob - mu_neg_dict[fn]) / sigma_neg_dict[fn]
                z_scores.append(z)
        if len(above) == 0:
            return "no_hit"
        elif len(above) == 1:
            return above[0]
        else:
            idx = np.argmax(z_scores)
            return above[idx]

    predicted_probs["function"] = predicted_probs.apply(assign_function_row, axis=1)
    predicted_probs["function_num"] = predicted_probs["function"].map(function_to_num)
    predicted_probs[["id", "function", "function_num"]].to_csv(out_dir, index=False)
    print(f"predicted_function.csv saved to {out_dir}")
    return predicted_probs[["id", "function", "function_num"]]


def strand_to_num(strand_series):
    return strand_series.map({"+": 1, "-": -1}).values


def window_with_direction(function_vector, strand_vector, window_size, step_size=1):
    import numpy as np

    windows = []
    directions = []
    indices = []
    for i in range(0, len(function_vector) - window_size + 1, step_size):
        func_win = function_vector[i : i + window_size]
        strand_win = strand_vector[i : i + window_size]
        strand_sum = np.sum(strand_win)
        if strand_sum < 0:
            # Reverse: flip the function vector for prediction
            windows.append(func_win[::-1])
            directions.append(False)  # False = reverse
        else:
            windows.append(func_win)
            directions.append(True)  # True = forward
        indices.append(i)
    return np.array(windows), np.array(directions), np.array(indices)


def discover_pici(
    data_dir, results_dir, model_function_path, model_pici_path, window_size
):
    import os
    import numpy as np
    import pandas as pd

    """
    Discover PICI segments in a genome.

    Args:
        data_dir (str): dataset directory
        results_dir (str): results directory
        model_function_path (str): folder directory for function prediction
        model_pici_path (str): file directory for PICI prediction
    """
    fasta_dir = os.path.join(data_dir, "protein.faa")
    gff_dir = os.path.join(data_dir, "genomic.gff")
    feature_out_dir = os.path.join(data_dir, "features.pa")
    gff_out_dir = os.path.join(data_dir, "gff_df.csv")
    predicted_prob_out_dir = os.path.join(results_dir, "predicted_prob.csv")
    predicted_function_out_dir = os.path.join(results_dir, "predicted_function.csv")
    pici_out_dir = os.path.join(results_dir, "pici_df.csv")
    img_dir = results_dir
    # Generate features
    feature_df = feature_generation(fasta_dir, feature_out_dir)
    # Parse GFF
    gff_df = parse_gff(gff_dir, gff_out_dir)
    # Predicted prob
    predicted_prob = predict_function(
        feature_df, predicted_prob_out_dir, model_function_path
    )
    # Assign functions
    from pici_predictor.phrog_function import (
        function_name_formatted_to_num,
        thresholds_b,
        mu_neg_dict,
        sigma_neg_dict,
    )

    predicted_function = assign_functions(
        predicted_prob,
        thresholds_b,
        mu_neg_dict,
        sigma_neg_dict,
        function_name_formatted_to_num,
        predicted_function_out_dir,
    )

    # windowing
    merged = gff_df.merge(
        predicted_function[["id", "function_num"]], on="id", how="inner"
    )
    merged = merged.sort_values(["contig", "start"]).reset_index(drop=True)
    function_vector = merged["function_num"].values
    strand_vector = strand_to_num(merged["strand"])

    windows, directions, indices = window_with_direction(
        function_vector, strand_vector, window_size
    )

    def predict_pici_segments(windows, model_path, threshold=0.4, class_names=None):
        import xgboost as xgb

        model = xgb.XGBClassifier()
        model.load_model(model_path)

        # Predict probabilities
        proba = model.predict_proba(windows)
        max_proba = np.max(proba, axis=1)
        max_class = np.argmax(proba, axis=1)
        predicted_class = np.where(max_proba >= threshold, max_class, 0)

        df = pd.DataFrame(
            proba, columns=[f"prob_class_{i}" for i in range(proba.shape[1])]
        )
        df["max_probability"] = max_proba
        df["predicted_class"] = predicted_class
        if class_names:
            df["predicted_class_name"] = [class_names[i] for i in predicted_class]
        return df

    class_names = ["none", "PICI", "CFPICI", "P4"]
    results = predict_pici_segments(
        windows, model_pici_path, threshold=0.4, class_names=class_names
    )
    results["forward"] = directions
    results["window_start_idx"] = indices

    merged.to_csv(os.path.join(results_dir, "merged.csv"), index=False)
    print("merged.csv saved")

    # visualization
    def plot_pici_segments_heatmap(segments_df, function_vector, img_dir, type):
        import matplotlib.pyplot as plt
        from matplotlib.colors import ListedColormap
        from pici_predictor.phrog_function import function_num_to_color
        import os
        import numpy as np

        # Prepare data
        heatmap_data = np.array(segments_df["function_vector"].tolist())

        # Print function vectors for inspection
        print(f"\nFunction vectors for {type}:")
        for i, row in segments_df.iterrows():
            print(f"Segment {i + 1}: {row['function_vector']}")
            print(
                f"Location: {row.start_contig}:{row.genome_start}-{row.genome_end}, {'reverse' if not row.forward else 'forward'}"
            )
            print(f"Probability: {row.predicted_prob:.3f}\n")

        labels = [
            f"proba={row.predicted_prob:.3f}, {row.start_contig}:{row.genome_start}-{row.genome_end}, {'reverse' if not row.forward else 'forward'}"
            for _, row in segments_df.iterrows()
        ]

        # Print color mapping for verification
        # print("\nColor mapping:")
        # for num, color in sorted(function_num_to_color.items()):
        #     print(f"Function {num}: {color}")

        # Create direct mapping colormap
        unique_nums = np.unique(heatmap_data)
        # Create colormap using a direct mapping
        colors = []
        for num in range(int(max(unique_nums)) + 1):
            if num in function_num_to_color:
                colors.append(function_num_to_color[num])
            else:
                colors.append("#FFFFFF")  # White for any missing numbers

        cmap = ListedColormap(colors)

        # Create plot
        fig, ax = plt.subplots(figsize=(5, len(heatmap_data) * 0.2))
        im = ax.imshow(
            heatmap_data, aspect="auto", cmap=cmap, vmin=0, vmax=len(colors) - 1
        )

        # Remove axes, ticks, and margins
        ax.axis("off")
        plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
        plt.margins(0, 0)
        plt.gca().xaxis.set_major_locator(plt.NullLocator())
        plt.gca().yaxis.set_major_locator(plt.NullLocator())

        # Add labels as text
        for i, label in enumerate(labels):
            ax.text(
                heatmap_data.shape[1]
                + 0.5,  # x position (just to the right of the heatmap)
                i,  # y position (row)
                label,
                va="center",
                ha="left",
                fontsize=9,
                color="black",
            )
        plt.title(f"{type}")

        # Save plot
        os.makedirs(img_dir, exist_ok=True)
        plt.savefig(
            os.path.join(img_dir, f"heatmap_{type}.png"),
            bbox_inches="tight",
            pad_inches=0,
            dpi=300,
        )

        # Display plot directly
        plt.show()
        plt.close()

    for type in ["PICI", "CFPICI", "P4"]:
        type_results = results[results["predicted_class_name"] == type].copy()
        if len(type_results) > 0:
            segments_df = prepare_predicted_segments(
                type_results, function_vector, window_size, merged
            )
            plot_pici_segments_heatmap(segments_df, function_vector, img_dir, type)

    # check
    # print(feature_df.head())
    # print(feature_df.shape)
    # print(gff_df.head())
    # print(gff_df.shape)
    # print(predicted_prob.head(10))
    # print(predicted_prob["dna_rna_and_nucleotide_metabolism"].mean())
    # print(predicted_prob.shape)
    print(predicted_function["function"].value_counts())
    # print(predicted_function.shape)
    # print(merged.head())
    # print(merged.shape)
    return results


def prepare_predicted_segments(results, function_vector, window_size, merged_df):
    import pandas as pd

    segments = []
    for idx, row in results.iterrows():
        start_idx = row["window_start_idx"]
        end_idx = start_idx + window_size - 1
        if end_idx >= len(function_vector):
            continue
        # Get genomic coordinates
        start_row = merged_df.iloc[start_idx]
        end_row = merged_df.iloc[end_idx]
        # For visualization, always show function_vector in the direction of the segment
        if row["forward"]:
            func_vec = function_vector[start_idx : end_idx + 1].tolist()
        else:
            func_vec = function_vector[start_idx : end_idx + 1][::-1].tolist()
        segment = {
            "function_vector": func_vec,
            "start_idx": start_idx,
            "end_idx": end_idx,
            "forward": row["forward"],
            "predicted_type": row["predicted_class_name"],
            "predicted_prob": row["max_probability"],
            "start_contig": start_row["contig"],
            "end_contig": end_row["contig"],
            "genome_start": min(start_row["start"], end_row["start"]),
            "genome_end": max(start_row["end"], end_row["end"]),
            "start_strand": start_row["strand"],
            "end_strand": end_row["strand"],
        }
        segments.append(segment)
    return pd.DataFrame(segments)
