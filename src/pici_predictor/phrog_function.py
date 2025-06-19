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

function_name_formatted_to_num = {
    "lysis": 1,
    "tail": 2,
    "connector": 3,
    "dna_rna_and_nucleotide_metabolism": 4,
    "head_and_packaging": 5,
    "other": 6,
    "transcription_regulation": 7,
    "moron_auxiliary_metabolic_gene_and_host_takeover": 8,
    "unknown_function": 9,
    "integration_and_excision": 10,
    "no_hit": 11,
}


function_colors = {
    # using formatted function names
    "lysis": "#f35f49",
    "tail": "#07e9a2",
    "connector": "#35d7ff",
    "dna_rna_and_nucleotide_metabolism": "#ffdf59",
    "head_and_packaging": "#3e83f6",
    "other": "#838383",
    "transcription_regulation": "#a861e3",
    "moron_auxiliary_metabolic_gene_and_host_takeover": "#ff59f5",
    "unknown_function": "#313131",  # dark grey
    "integration_and_excision": "#fea328",
    "no_hit": "#f5f5f5",  # light grey
}

function_num_to_color = {
    1: "#f35f49",
    2: "#07e9a2",
    3: "#35d7ff",
    4: "#ffdf59",
    5: "#3e83f6",
    6: "#838383",
    7: "#a861e3",
    8: "#ff59f5",
    9: "#313131",
    10: "#fea328",
    11: "#f5f5f5",
}

thresholds_optimal = {
    "lysis": 0.06,
    "tail": 0.03,
    "connector": 0.03,
    "dna_rna_and_nucleotide_metabolism": 0.04,
    "head_and_packaging": 0.01,
    "other": 0.01,
    "transcription_regulation": 0.01,
    "moron_auxiliary_metabolic_gene_and_host_takeover": 0.01,
    "unknown_function": 0.29,
    "integration_and_excision": 0.23,
}

thresholds_0_5 = {
    "lysis": 0.5,
    "tail": 0.5,
    "connector": 0.5,
    "dna_rna_and_nucleotide_metabolism": 0.5,
    "head_and_packaging": 0.5,
    "other": 0.5,
    "transcription_regulation": 0.5,
    "moron_auxiliary_metabolic_gene_and_host_takeover": 0.5,
    "unknown_function": 0.5,
    "integration_and_excision": 0.5,
}

thresholds_0_3 = {
    "lysis": 0.3,
    "tail": 0.3,
    "connector": 0.3,
    "dna_rna_and_nucleotide_metabolism": 0.3,
    "head_and_packaging": 0.3,
    "other": 0.3,
    "transcription_regulation": 0.3,
    "moron_auxiliary_metabolic_gene_and_host_takeover": 0.3,
    "unknown_function": 0.3,
    "integration_and_excision": 0.3,
}

thresholds_a = {
    "lysis": 0.05,
    "tail": 0.05,
    "connector": 0.1,
    "dna_rna_and_nucleotide_metabolism": 0.3,
    "head_and_packaging": 0.05,
    "other": 0.3,
    "transcription_regulation": 0.1,
    "moron_auxiliary_metabolic_gene_and_host_takeover": 0.99,
    "unknown_function": 0.7,
    "integration_and_excision": 0.05,
}

thresholds_b = {
    "lysis": 0.7,
    "tail": 0.7,
    "connector": 0.7,
    "dna_rna_and_nucleotide_metabolism": 0.7,
    "head_and_packaging": 0.7,
    "other": 0.7,
    "transcription_regulation": 0.9,
    "moron_auxiliary_metabolic_gene_and_host_takeover": 0.99,
    "unknown_function": 0.7,
    "integration_and_excision": 0.7,
}

# z-score params
mu_neg_dict = {
    "lysis": 0.00064970204,
    "tail": 7.0620925e-05,
    "connector": 5.0706547e-07,
    "dna_rna_and_nucleotide_metabolism": 0.85884595,
    "head_and_packaging": 0.00034330788,
    "other": 6.0434857e-05,
    "transcription_regulation": 4.5458604e-10,
    "moron_auxiliary_metabolic_gene_and_host_takeover": 0.040228892,
    "unknown_function": 0.0011214364,
    "integration_and_excision": 2.400698e-05,
}

sigma_neg_dict = {
    "lysis": 0.00022949721,
    "tail": 1.9761694e-05,
    "connector": 1.7011082e-07,
    "dna_rna_and_nucleotide_metabolism": 0.044518474,
    "head_and_packaging": 0.00016175798,
    "other": 3.049463e-05,
    "transcription_regulation": 2.1637066e-10,
    "moron_auxiliary_metabolic_gene_and_host_takeover": 0.009698894,
    "unknown_function": 0.00057164463,
    "integration_and_excision": 1.7930515e-05,
}

# pici types
type_to_num = {
    "phage": 0,
    "PICI": 1,
    "CFPICI": 2,
    "P4": 3,
}
