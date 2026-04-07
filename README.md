## Machine learning-based discovery of phage-inducible chromosomal islands (PICIs) from protein functional patterns.

The project develops an end-to-end machine learning pipeline for identifying PICI-related elements in bacterial genomes using protein functional patterns rather than sequence homology.

The workflow consists of two main stages:

1. protein-level function prediction based on biological feature engineering and supervised learning
2. genome-level identification of PICI-related elements from predicted functional patterns

The protein-function modeling stage uses high-dimensional sequence-derived features and XGBoost classifiers trained on curated phage and phage-satellite protein data. The downstream identification stage uses predicted function patterns to distinguish PICI-related elements from non-satellite regions.

This project was developed as an alternative to homology-based detection, with the goal of improving discovery of diverse or previously uncharacterized PICI-related elements.
