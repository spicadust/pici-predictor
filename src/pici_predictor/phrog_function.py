function_names_raw = [
    "unknown_no_hit",
    "DNA, RNA and nucleotide metabolism",
    "tail",
    "head and packaging",
    "connector",
    "lysis",
    "transcription regulation",
    "integration and excision",
    "other",
    "moron, auxiliary metabolic gene and host takeover",
    "unknown function",
]

function_names_formatted = [
    "lysis",
    "tail",
    "connector",
    "dna_rna_and_nucleotide_metabolism",
    "head_and_packaging",
    "other",
    "transcription_regulation",
    "moron_auxiliary_metabolic_gene_and_host_takeover",
    "unknown_function",
    "integration_and_excision",
    "no_hit",
]

function_name_raw_to_formatted = {
    "DNA, RNA and nucleotide metabolism": "dna_rna_and_nucleotide_metabolism",
    "head and packaging": "head_and_packaging",
    "transcription regulation": "transcription_regulation",
    "integration and excision": "integration_and_excision",
    "moron, auxiliary metabolic gene and host takeover": "moron_auxiliary_metabolic_gene_and_host_takeover",
    "unknown function": "unknown_function",
    "unknown_no_hit": "no_hit",
    "lysis": "lysis",
    "connector": "connector",
    "tail": "tail",
    "other": "other",
}

function_name_raw_to_abbreviation = {
    "lysis": "lysis",
    "tail": "tail",
    "connector": "conn",
    "DNA, RNA and nucleotide metabolism": "dna_rna",
    "head and packaging": "head",
    "integration and excision": "int_exc",
    "transcription regulation": "trans",
    "unknown function": "unkn",
    "moron, auxiliary metabolic gene and host takeover": "moron",
    "unknown_no_hit": "no_hit",
}

function_name_raw_to_num = {
    "lysis": 1,
    "tail": 2,
    "connector": 3,
    "DNA, RNA and nucleotide metabolism": 4,
    "head and packaging": 5,
    "other": 6,
    "transcription regulation": 7,
    "moron, auxiliary metabolic gene and host takeover": 8,
    "unknown function": 9,
    "integration and excision": 10,
    "unknown_no_hit": 11,
}
