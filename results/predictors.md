ROC AUC: Receiver Operating Characteristic Area Under the Curve  
Accuracy = (True Positives + True Negatives) / Total Predictions  
Precision = True Positives / (True Positives + False Positives)  
Recall = True Positives / (True Positives + False Negatives)  
F1 = 2 * (Precision * Recall) / (Precision + Recall)
MCC = (TP × TN - FP × FN) / √((TP + FP) × (TP + FN) × (TN + FP) × (TN + FN))

## tail

label
0    286131
1     74282

Top 20 most important features:
BP:prop_res_Basic: 0.0268
BP:prop_res_Charged: 0.0123
HTS-T:2: 0.0088
RED_DIPEP:CC: 0.0056
BP:prop_res_Small: 0.0050
BP:percent:C: 0.0049
BP:molecular_weight: 0.0048
BP:percent_helix_naive: 0.0048
BP:length: 0.0045
RED_TRIPEP:HAH: 0.0043
RED_TRIPEP:SCC: 0.0043
BP:percent:T: 0.0041
RED_TRIPEP:LKC: 0.0040
RED_TRIPEP:CCE: 0.0037
RED_TRIPEP:SFH: 0.0034
BP:percent:H: 0.0031
BP:isoelectric_point: 0.0030
RED_DIPEP:CL: 0.0029
RED_DIPEP:HC: 0.0029
RED_TRIPEP:HPL: 0.0028

=== Training Set ===

Metrics for train (threshold=0.5):
train_accuracy: 0.9880
train_precision: 0.9496
train_recall: 0.9923
train_f1: 0.9705
train_roc_auc: 0.9993
train_mcc: 0.9633

Confusion Matrix Values:
P: 36_159 Tp: 35_880 Fp: 1_906 N: 146_499 Tn: 144_593 Fn: 279

=== Validation Set ===

Metrics for val (threshold=0.5):
val_accuracy: 0.8902
val_precision: 0.7647
val_recall: 0.7830
val_f1: 0.7737
val_roc_auc: 0.9258
val_mcc: 0.7014

Confusion Matrix Values:
P: 26_915 Tp: 21_074 Fp: 6_486 N: 85_383 Tn: 78_897 Fn: 5_841

=== Test Set ===

Metrics for test (threshold=0.3):
test_accuracy: 0.8339
test_precision: 0.5097
test_recall: 0.7810
test_f1: 0.6169
test_roc_auc: 0.8786
test_mcc: 0.5359

Confusion Matrix Values:
P: 11_208 Tp: 8_754 Fp: 8_420 N: 54_249 Tn: 45_829 Fn: 2_454

Metrics for test (threshold=0.4):
test_accuracy: 0.8552
test_precision: 0.5603
test_recall: 0.7159
test_f1: 0.6286
test_roc_auc: 0.8786
test_mcc: 0.5466

Confusion Matrix Values:
P: 11_208 Tp: 8_024 Fp: 6_297 N: 54_249 Tn: 47_952 Fn: 3_184

Metrics for test (threshold=0.5):
test_accuracy: 0.8681
test_precision: 0.6061
test_recall: 0.6556
test_f1: 0.6299
test_roc_auc: 0.8786
**test_mcc: 0.5504**

Confusion Matrix Values:
P: 11_208 Tp: 7_348 Fp: 4_775 N: 54_249 Tn: 49_474 Fn: 3_860

Metrics for test (threshold=0.6):
test_accuracy: 0.8764
test_precision: 0.6529
test_recall: 0.5945
test_f1: 0.6223
test_roc_auc: 0.8786
test_mcc: 0.5495

Confusion Matrix Values:
P: 11_208 Tp: 6_663 Fp: 3_543 N: 54_249 Tn: 50_706 Fn: 4_545

Metrics for test (threshold=0.7):
test_accuracy: 0.8800
test_precision: 0.6995
test_recall: 0.5242
test_f1: 0.5993
test_roc_auc: 0.8786
test_mcc: 0.5380

Confusion Matrix Values:
P: 11_208 Tp: 5_875 Fp: 2_524 N: 54_249 Tn: 51_725 Fn: 5_333

## lysis

label
0    339951
1     20462

Top 20 most important features:
BP:prop_res_Non-polar: 0.0124
RED_TRIPEP:HLC: 0.0109
BP:isoelectric_point: 0.0104
DIPEP:AV: 0.0058
DIPEP:VK: 0.0054
RED_TRIPEP:PHS: 0.0052
RED_TRIPEP:ACS: 0.0052
RED_TRIPEP:GLH: 0.0051
RED_TRIPEP:PSK: 0.0050
BP:prop_res_Polar: 0.0050
RED_TRIPEP:PCK: 0.0047
BP:molecular_weight: 0.0045
RED_TRIPEP:CKF: 0.0044
RED_TRIPEP:PPC: 0.0042
BP:prop_res_Aliphatic: 0.0041
BP:length: 0.0041
RED_TRIPEP:ASH: 0.0040
RED_TRIPEP:FPL: 0.0038
RED_DIPEP:PC: 0.0037
RED_DIPEP:FC: 0.0037

=== Training Set ===

Metrics for train (threshold=0.5):
train_accuracy: 0.9984
train_precision: 0.9680
train_recall: 1.0000
train_f1: 0.9838
train_roc_auc: 1.0000
train_mcc: 0.9830

Confusion Matrix Values:
P: 8_963 Tp: 8_963 Fp: 296 N: 173_695 Tn: 173_399 Fn: 0

=== Validation Set ===

Metrics for val (threshold=0.5):
val_accuracy: 0.9320
val_precision: 0.6837
val_recall: 0.2083
val_f1: 0.3193
val_roc_auc: 0.8532
val_mcc: 0.3529

Confusion Matrix Values:
P: 8_593 Tp: 1_790 Fp: 828 N: 103_705 Tn: 102_877 Fn: 6_803

=== Test Set ===

Metrics for test (threshold=0.3):
test_accuracy: 0.9586
test_precision: 0.5321
test_recall: 0.5530
test_f1: 0.5424
test_roc_auc: 0.9073
test_mcc: 0.5208

Confusion Matrix Values:
P: 2_906 Tp: 1_607 Fp: 1_413 N: 62_551 Tn: 61_138 Fn: 1_299

Metrics for test (threshold=0.4):
test_accuracy: 0.9640
test_precision: 0.6122
test_recall: 0.5165
test_f1: 0.5603
test_roc_auc: 0.9073
test_mcc: 0.5438

Confusion Matrix Values:
P: 2_906 Tp: 1_501 Fp: 951 N: 62_551 Tn: 61_600 Fn: 1_405

Metrics for test (threshold=0.5):
test_accuracy: 0.9661
test_precision: 0.6641
test_recall: 0.4776
test_f1: 0.5556
test_roc_auc: 0.9073
test_mcc: 0.5464

Confusion Matrix Values:
P: 2_906 Tp: 1_388 Fp: 702 N: 62_551 Tn: 61_849 Fn: 1_518

Metrics for test (threshold=0.6):
test_accuracy: 0.9666
test_precision: 0.6986
test_recall: 0.4346
test_f1: 0.5359
test_roc_auc: 0.9073
test_mcc: 0.5353

Confusion Matrix Values:
P: 2_906 Tp: 1_263 Fp: 545 N: 62_551 Tn: 62_006 Fn: 1_643

Metrics for test (threshold=0.7):
test_accuracy: 0.9661
test_precision: 0.7203
test_recall: 0.3882
test_f1: 0.5045
test_roc_auc: 0.9073
test_mcc: 0.5138

Confusion Matrix Values:
P: 2_906 Tp: 1_128 Fp: 438 N: 62_551 Tn: 62_113 Fn: 1_778

## transcription_regulation
label
0    345491
1     14922

Top 20 most important features:
BP:length: 0.0205
HTS-T:2: 0.0143
BP:molecular_weight: 0.0104
BP:molar_extinction_coefficient_cysteines: 0.0066
RED_TRIPEP:HSA: 0.0059
BP:prop_res_Basic: 0.0051
RED_DIPEP:CH: 0.0044
RED_TRIPEP:CPS: 0.0041
RED_TRIPEP:LAC: 0.0040
RED_DIPEP:GA: 0.0039
BP:prop_res_Charged: 0.0037
RED_TRIPEP:GKF: 0.0034
RED_DIPEP:CP: 0.0034
DIPEP:CP: 0.0034
BP:prop_res_Small: 0.0031
RED_TRIPEP:PFL: 0.0031
DIPEP:GA: 0.0031
BP:percent:G: 0.0029
BP:prop_res_Aromatic: 0.0029
RED_TRIPEP:ELA: 0.0028

=== Training Set ===

Metrics for train (threshold=0.5):
train_accuracy: 0.9935
train_precision: 0.8933
train_recall: 1.0000
train_f1: 0.9436
train_roc_auc: 1.0000
train_mcc: 0.9419

Confusion Matrix Values:
P: 9_976 Tp: 9_976 Fp: 1_192 N: 172_682 Tn: 171_490 Fn: 0

=== Validation Set ===

Metrics for val (threshold=0.5):
val_accuracy: 0.9660
val_precision: 0.4237
val_recall: 0.4680
val_f1: 0.4448
val_roc_auc: 0.9204
val_mcc: 0.4279

Confusion Matrix Values:
P: 3_265 Tp: 1_528 Fp: 2_078 N: 109_033 Tn: 106_955 Fn: 1_737

=== Test Set ===

Metrics for test (threshold=0.3):
test_accuracy: 0.9086
test_precision: 0.1728
test_recall: 0.6764
test_f1: 0.2753
test_roc_auc: 0.9221
test_mcc: 0.3109

Confusion Matrix Values:
P: 1_681 Tp: 1_137 Fp: 5_442 N: 63_776 Tn: 58_334 Fn: 544

Metrics for test (threshold=0.4):
test_accuracy: 0.9325
test_precision: 0.2133
test_recall: 0.6050
test_f1: 0.3153
test_roc_auc: 0.9221
test_mcc: 0.3324

Confusion Matrix Values:
P: 1_681 Tp: 1_017 Fp: 3_752 N: 63_776 Tn: 60_024 Fn: 664

Metrics for test (threshold=0.5):
test_accuracy: 0.9488
test_precision: 0.2558
test_recall: 0.5211
test_f1: 0.3431
test_roc_auc: 0.9221
test_mcc: 0.3418

Confusion Matrix Values:
P: 1_681 Tp: 876 Fp: 2_549 N: 63_776 Tn: 61_227 Fn: 805

Metrics for test (threshold=0.6):
test_accuracy: 0.9626
test_precision: 0.3289
test_recall: 0.4396
test_f1: 0.3763
test_roc_auc: 0.9221
test_mcc: 0.3614

Confusion Matrix Values:
P: 1_681 Tp: 739 Fp: 1_508 N: 63_776 Tn: 62_268 Fn: 942

Metrics for test (threshold=0.7):
test_accuracy: 0.9725
test_precision: 0.4529
test_recall: 0.3373
test_f1: 0.3866
test_roc_auc: 0.9221
test_mcc: 0.3771

Confusion Matrix Values:
P: 1_681 Tp: 567 Fp: 685 N: 63_776 Tn: 63_091 Fn: 1_114

## dna_rna_and_nucleotide_metabolism
Top 20 most important features:
BP:prop_res_Basic: 0.0153
BP:prop_res_Charged: 0.0080
BP:percent:C: 0.0056
entropyAA: 0.0053
RED_TRIPEP:CPG: 0.0048
DIPEP:PC: 0.0039
RED_TRIPEP:CAF: 0.0038
RED_TRIPEP:KCC: 0.0037
RED_TRIPEP:GCP: 0.0037
RED_TRIPEP:KCH: 0.0034
BP:percent:H: 0.0031
RED_TRIPEP:CHP: 0.0027
RED_TRIPEP:KCF: 0.0026
HTS-T:2: 0.0024
BP:molar_extinction_coefficient_cysteines: 0.0024
BP:prop_res_Aromatic: 0.0024
RED_TRIPEP:SPG: 0.0023
RED_TRIPEP:SGH: 0.0023
RED_TRIPEP:PGG: 0.0023
RED_DIPEP:PC: 0.0021

=== Training Set ===

Metrics for train (threshold=0.5):
train_accuracy: 0.9729
train_precision: 0.9284
train_recall: 0.9766
train_f1: 0.9519
train_roc_auc: 0.9969
train_mcc: 0.9336

Confusion Matrix Values:
P: 50_137 Tp: 48_965 Fp: 3_776 N: 132_521 Tn: 128_745 Fn: 1_172

=== Validation Set ===

Metrics for val (threshold=0.5):
val_accuracy: 0.7683
val_precision: 0.5642
val_recall: 0.6688
val_f1: 0.6120
val_roc_auc: 0.8379
val_mcc: 0.4519

Confusion Matrix Values:
P: 30_690 Tp: 20_526 Fp: 15_857 N: 81_608 Tn: 65_751 Fn: 10_164

=== Test Set ===

Metrics for test (threshold=0.3):
test_accuracy: 0.7313
test_precision: 0.5890
test_recall: 0.8540
test_f1: 0.6972
test_roc_auc: 0.8501
test_mcc: 0.4963

Confusion Matrix Values:
P: 23_704 Tp: 20_243 Fp: 14_125 N: 41_753 Tn: 27_628 Fn: 3_461

Metrics for test (threshold=0.4):
test_accuracy: 0.7577
test_precision: 0.6356
test_recall: 0.7754
test_f1: 0.6986
test_roc_auc: 0.8501
test_mcc: 0.5062

Confusion Matrix Values:
P: 23_704 Tp: 18_380 Fp: 10_538 N: 41_753 Tn: 31_215 Fn: 5_324

Metrics for test (threshold=0.5):
test_accuracy: 0.7725
test_precision: 0.6854
test_recall: 0.6869
test_f1: 0.6862
test_roc_auc: 0.8501
test_mcc: 0.5077

Confusion Matrix Values:
P: 23_704 Tp: 16_283 Fp: 7_473 N: 41_753 Tn: 34_280 Fn: 7_421

Metrics for test (threshold=0.6):
test_accuracy: 0.7721
test_precision: 0.7303
test_recall: 0.5876
test_f1: 0.6512
test_roc_auc: 0.8501
test_mcc: 0.4912

Confusion Matrix Values:
P: 23_704 Tp: 13_929 Fp: 5_144 N: 41_753 Tn: 36_609 Fn: 9_775

Metrics for test (threshold=0.7):
test_accuracy: 0.7558
test_precision: 0.7721
test_recall: 0.4619
test_f1: 0.5780
test_roc_auc: 0.8501
test_mcc: 0.4486

Confusion Matrix Values:
P: 23_704 Tp: 10_948 Fp: 3_231 N: 41_753 Tn: 38_522 Fn: 12_756

## head_and_packaging
Top 20 most important features:
BP:percent:C: 0.0087
BP:prop_res_Aromatic: 0.0061
BP:percent:H: 0.0051
RED_TRIPEP:CCH: 0.0047
RED_TRIPEP:PHK: 0.0044
BP:isoelectric_point: 0.0041
DIPEP:MC: 0.0041
RED_TRIPEP:CFA: 0.0039
BP:molecular_weight: 0.0036
BP:prop_res_Basic: 0.0035
RED_TRIPEP:CKC: 0.0033
RED_DIPEP:EA: 0.0032
HTS-T:2: 0.0032
BP:length: 0.0032
RED_TRIPEP:HSG: 0.0030
RED_TRIPEP:CSL: 0.0029
RED_TRIPEP:KCH: 0.0028
BP:percent_strand_naive: 0.0027
RED_TRIPEP:HPL: 0.0025
RED_TRIPEP:CKK: 0.0024

=== Training Set ===

Metrics for train (threshold=0.5):
train_accuracy: 0.9788
train_precision: 0.9072
train_recall: 0.9833
train_f1: 0.9437
train_roc_auc: 0.9983
train_mcc: 0.9318

Confusion Matrix Values:
P: 33_031 Tp: 32_478 Fp: 3_322 N: 149_627 Tn: 146_305 Fn: 553

=== Validation Set ===

Metrics for val (threshold=0.5):
val_accuracy: 0.8197
val_precision: 0.5463
val_recall: 0.4974
val_f1: 0.5207
val_roc_auc: 0.8006
val_mcc: 0.4106

Confusion Matrix Values:
P: 22_113 Tp: 10_999 Fp: 9_135 N: 90_185 Tn: 81_050 Fn: 11_114

=== Test Set ===

Metrics for test (threshold=0.3):
test_accuracy: 0.7717
test_precision: 0.3970
test_recall: 0.7520
test_f1: 0.5196
test_roc_auc: 0.8470
test_mcc: 0.4222

Confusion Matrix Values:
P: 10_750 Tp: 8_084 Fp: 12_281 N: 54_707 Tn: 42_426 Fn: 2_666

Metrics for test (threshold=0.4):
test_accuracy: 0.8234
test_precision: 0.4736
test_recall: 0.6767
test_f1: 0.5573
test_roc_auc: 0.8470
test_mcc: 0.4624

Confusion Matrix Values:
P: 10_750 Tp: 7_275 Fp: 8_085 N: 54_707 Tn: 46_622 Fn: 3_475

Metrics for test (threshold=0.5):
test_accuracy: 0.8569
test_precision: 0.5613
test_recall: 0.5901
test_f1: 0.5753
test_roc_auc: 0.8470
test_mcc: 0.4896

Confusion Matrix Values:
P: 10_750 Tp: 6_344 Fp: 4_959 N: 54_707 Tn: 49_748 Fn: 4_406

Metrics for test (threshold=0.6):
test_accuracy: 0.8772
test_precision: 0.6738
test_recall: 0.4890
test_f1: 0.5667
test_roc_auc: 0.8470
test_mcc: 0.5060

Confusion Matrix Values:
P: 10_750 Tp: 5_257 Fp: 2_545 N: 54_707 Tn: 52_162 Fn: 5_493

Metrics for test (threshold=0.7):
test_accuracy: 0.8818
test_precision: 0.7909
test_recall: 0.3813
test_f1: 0.5145
test_roc_auc: 0.8470
test_mcc: 0.4960

Confusion Matrix Values:
P: 10_750 Tp: 4_099 Fp: 1_084 N: 54_707 Tn: 53_623 Fn: 6_651

## integration_and_excision
Top 20 most important features:
BP:prop_res_Basic: 0.0218
BP:isoelectric_point: 0.0094
RED_TRIPEP:PSC: 0.0090
DIPEP:SD: 0.0081
BP:length: 0.0080
BP:percent:R: 0.0072
BP:percent:C: 0.0071
RED_TRIPEP:KKH: 0.0070
BP:molecular_weight: 0.0057
RED_TRIPEP:AFH: 0.0051
RED_TRIPEP:FCC: 0.0047
RED_TRIPEP:FKP: 0.0043
RED_TRIPEP:HCG: 0.0043
RED_DIPEP:KK: 0.0039
RED_TRIPEP:SCK: 0.0039
DIPEP:DH: 0.0038
BP:molar_extinction_coefficient_cysteines: 0.0038
RED_TRIPEP:HSL: 0.0036
RED_TRIPEP:CCL: 0.0034
DIPEP:TC: 0.0033

=== Training Set ===

Metrics for train (threshold=0.5):
train_accuracy: 0.9995
train_precision: 0.9789
train_recall: 1.0000
train_f1: 0.9893
train_roc_auc: 1.0000
train_mcc: 0.9892

Confusion Matrix Values:
P: 4_273 Tp: 4_273 Fp: 92 N: 178_385 Tn: 178_293 Fn: 0

=== Validation Set ===

Metrics for val (threshold=0.5):
val_accuracy: 0.9889
val_precision: 0.7159
val_recall: 0.7507
val_f1: 0.7329
val_roc_auc: 0.9781
val_mcc: 0.7274

Confusion Matrix Values:
P: 2_286 Tp: 1_716 Fp: 681 N: 110_012 Tn: 109_331 Fn: 570

=== Test Set ===

Metrics for test (threshold=0.3):
test_accuracy: 0.9842
test_precision: 0.3861
test_recall: 0.3037
test_f1: 0.3399
test_roc_auc: 0.8557
test_mcc: 0.3345

Confusion Matrix Values:
P: 876 Tp: 266 Fp: 423 N: 64_581 Tn: 64_158 Fn: 610

Metrics for test (threshold=0.4):
test_accuracy: 0.9853
test_precision: 0.4095
test_recall: 0.2272
test_f1: 0.2922
test_roc_auc: 0.8557
test_mcc: 0.2981

Confusion Matrix Values:
P: 876 Tp: 199 Fp: 287 N: 64_581 Tn: 64_294 Fn: 677

Metrics for test (threshold=0.5):
test_accuracy: 0.9860
test_precision: 0.4466
test_recall: 0.1815
test_f1: 0.2581
test_roc_auc: 0.8557
test_mcc: 0.2788

Confusion Matrix Values:
P: 876 Tp: 159 Fp: 197 N: 64_581 Tn: 64_384 Fn: 717

Metrics for test (threshold=0.6):
test_accuracy: 0.9865
test_precision: 0.4874
test_recall: 0.1541
test_f1: 0.2342
test_roc_auc: 0.8557
test_mcc: 0.2689

Confusion Matrix Values:
P: 876 Tp: 135 Fp: 142 N: 64_581 Tn: 64_439 Fn: 741

Metrics for test (threshold=0.7):
test_accuracy: 0.9864
test_precision: 0.4712
test_recall: 0.1119
test_f1: 0.1808
test_roc_auc: 0.8557
test_mcc: 0.2249

Confusion Matrix Values:
P: 876 Tp: 98 Fp: 110 N: 64_581 Tn: 64_471 Fn: 778