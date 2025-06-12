def parse_fasta_file(out_dir, df, id_col, seq_col):
    with open(out_dir, "w") as f:
        for idx, row in df.iterrows():
            f.write(f">{row[id_col]}\n")
            f.write(f"{row[seq_col]}\n")
    return out_dir


def parse_gff(gff_dir):
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
                        "protein_id": protein_id,
                        "contig": contig,
                        "start": start,
                        "end": end,
                        "strand": strand,
                    }
                )
    gff_df = (
        pd.DataFrame(records).sort_values(["contig", "start"]).reset_index(drop=True)
    )
    return gff_df


def feature_generation(fasta_dir, out_dir):
    import pandas as pd
    from tqdm import tqdm
    from Bio.SeqIO.FastaIO import SimpleFastaParser
    from feature_generation import seq2features
    import warnings
    from Bio import BiopythonDeprecationWarning
    import os

    warnings.filterwarnings("ignore", category=BiopythonDeprecationWarning)

    def load_sequences(fasta_file):
        try:
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
        except FileNotFoundError:
            raise FileNotFoundError(f"FASTA file not found: {fasta_file}")
        except Exception as e:
            raise Exception(f"Error loading sequences from {fasta_file}: {str(e)}")

    def generate_features(entries, chunk_size=100):
        try:
            features_list = []
            for i in tqdm(
                range(0, len(entries), chunk_size), desc="Feature extraction"
            ):
                chunk = entries[i : i + chunk_size]
                features_chunk = seq2features(chunk, min_length=10, scaling=True)
                features_list.append(features_chunk)
            return pd.concat(features_list)
        except Exception as e:
            raise Exception(f"Error generating features: {str(e)}")

    def save_results(features_df, output_file):
        try:
            # Create output directory if it doesn't exist
            os.makedirs(os.path.dirname(output_file), exist_ok=True)

            features_df = features_df.reset_index().rename(columns={"index": "id"})
            features_df = features_df.drop(columns=["md5"])
            features_df.to_parquet(output_file)
            print(f"Features saved to {output_file}")
        except Exception as e:
            raise Exception(f"Error saving results to {output_file}: {str(e)}")

    # Load sequences
    entries = load_sequences(fasta_dir)

    # Generate features
    features_df = generate_features(entries)

    # Save results
    save_results(features_df, out_dir)
    return out_dir
