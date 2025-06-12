def parse_fasta_file(out_dir, df, id_col, seq_col):
    with open(out_dir, "w") as f:
        for idx, row in df.iterrows():
            f.write(f">{row[id_col]}\n")
            f.write(f"{row[seq_col]}\n")
    return out_dir
