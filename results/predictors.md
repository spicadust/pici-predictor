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
test_mcc: 0.5504

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