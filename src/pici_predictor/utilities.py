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
    return predicted_probs[["id", "function", "function_num"]]


def window_vector(vec, window_size=30, step_size=1):
    import numpy as np

    windows = []
    indices = []
    for i in range(0, len(vec) - window_size + 1, step_size):
        windows.append(vec[i : i + window_size])
        indices.append(i)
    return np.array(windows), np.array(indices)


def discover_pici(data_dir, results_dir, model_function_path, model_pici_path):
    import os
    import numpy as np
    import pandas as pd

    fasta_dir = os.path.join(data_dir, "protein.faa")
    gff_dir = os.path.join(data_dir, "genomic.gff")
    feature_out_dir = os.path.join(data_dir, "features.pa")
    gff_out_dir = os.path.join(data_dir, "gff_df.csv")
    predicted_prob_out_dir = os.path.join(results_dir, "predicted_prob.csv")
    predicted_function_out_dir = os.path.join(results_dir, "predicted_function.csv")
    pici_out_dir = os.path.join(results_dir, "pici_df.csv")

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
        thresholds_0_5,
        mu_neg_dict,
        sigma_neg_dict,
    )

    predicted_function = assign_functions(
        predicted_prob,
        thresholds_0_5,
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

    # Forward windows
    forward_windows, forward_indices = window_vector(
        function_vector, window_size=30, step_size=1
    )
    # Reverse windows
    reverse_vector = function_vector[::-1]
    reverse_windows, reverse_indices = window_vector(
        reverse_vector, window_size=30, step_size=1
    )

    def predict_pici_segments(windows, model_path, threshold=0.4, class_names=None):
        import xgboost as xgb
        import pandas as pd

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
    forward_results = predict_pici_segments(
        forward_windows, model_pici_path, threshold=0.4, class_names=class_names
    )
    reverse_results = predict_pici_segments(
        reverse_windows, model_pici_path, threshold=0.4, class_names=class_names
    )
    forward_results["forward"] = True
    reverse_results["forward"] = False
    results = pd.concat([forward_results, reverse_results])
    results.to_csv(pici_out_dir, index=False)

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
