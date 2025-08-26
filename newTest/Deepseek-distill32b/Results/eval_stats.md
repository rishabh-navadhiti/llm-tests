# Evaluation Statistics Deepseek

## Field: PATIENT_NAME

### Metric: bleu_score
- Mean: 0.0000
- Std Dev: 0.0000
- Variance: 0.0000
- Shapiro-Wilk: statistic=1.0000, p=1.0000
- Kolmogorov-Smirnov: statistic=0.5000, p=0.0000
- Anderson-Darling: statistic=nan
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_analysis
- Mean: 0.3176
- Std Dev: 0.4364
- Variance: 0.1904
- Shapiro-Wilk: statistic=0.6697, p=0.0000
- Kolmogorov-Smirnov: statistic=0.3667, p=0.0001
- Anderson-Darling: statistic=5.3400
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_similarity
- Mean: 0.6021
- Std Dev: 0.3889
- Variance: 0.1513
- Shapiro-Wilk: statistic=0.7536, p=0.0000
- Kolmogorov-Smirnov: statistic=0.2356, p=0.0342
- Anderson-Darling: statistic=3.5972
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: rhetorical_similarity
- Mean: 0.5932
- Std Dev: 0.3854
- Variance: 0.1485
- Shapiro-Wilk: statistic=0.7633, p=0.0000
- Kolmogorov-Smirnov: statistic=0.2323, p=0.0383
- Anderson-Darling: statistic=3.4193
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: topic_similarity
- Mean: 0.5970
- Std Dev: 0.3620
- Variance: 0.1310
- Shapiro-Wilk: statistic=0.8417, p=0.0002
- Kolmogorov-Smirnov: statistic=0.2187, p=0.0598
- Anderson-Darling: statistic=2.0723
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Covariance Matrix (across metrics)

| Metric | bleu_score | content_analysis | content_similarity | rhetorical_similarity | topic_similarity |
| --- | --- | --- | --- | --- | --- |
| bleu_score | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| content_analysis | 0.0000 | 0.1904 | 0.1167 | 0.1163 | 0.0963 |
| content_similarity | 0.0000 | 0.1167 | 0.1513 | 0.1493 | 0.0021 |
| rhetorical_similarity | 0.0000 | 0.1163 | 0.1493 | 0.1485 | 0.0022 |
| topic_similarity | 0.0000 | 0.0963 | 0.0021 | 0.0022 | 0.1310 |

## Field: CHIEF_COMPLAINT

### Metric: bleu_score
- Mean: 0.0000
- Std Dev: 0.0000
- Variance: 0.0000
- Shapiro-Wilk: statistic=1.0000, p=1.0000
- Kolmogorov-Smirnov: statistic=0.5000, p=0.0000
- Anderson-Darling: statistic=nan
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_analysis
- Mean: 0.5655
- Std Dev: 0.4046
- Variance: 0.1637
- Shapiro-Wilk: statistic=0.8315, p=0.0001
- Kolmogorov-Smirnov: statistic=0.2014, p=0.1013
- Anderson-Darling: statistic=1.9999
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_similarity
- Mean: 0.6945
- Std Dev: 0.3713
- Variance: 0.1379
- Shapiro-Wilk: statistic=0.7469, p=0.0000
- Kolmogorov-Smirnov: statistic=0.2780, p=0.0070
- Anderson-Darling: statistic=3.6642
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: rhetorical_similarity
- Mean: 0.6923
- Std Dev: 0.3525
- Variance: 0.1242
- Shapiro-Wilk: statistic=0.7975, p=0.0000
- Kolmogorov-Smirnov: statistic=0.2364, p=0.0333
- Anderson-Darling: statistic=2.8874
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: topic_similarity
- Mean: 0.6142
- Std Dev: 0.4039
- Variance: 0.1631
- Shapiro-Wilk: statistic=0.7515, p=0.0000
- Kolmogorov-Smirnov: statistic=0.3153, p=0.0014
- Anderson-Darling: statistic=3.6851
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Covariance Matrix (across metrics)

| Metric | bleu_score | content_analysis | content_similarity | rhetorical_similarity | topic_similarity |
| --- | --- | --- | --- | --- | --- |
| bleu_score | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| content_analysis | 0.0000 | 0.1637 | 0.1320 | 0.1197 | 0.0672 |
| content_similarity | 0.0000 | 0.1320 | 0.1379 | 0.1283 | 0.0366 |
| rhetorical_similarity | 0.0000 | 0.1197 | 0.1283 | 0.1242 | 0.0365 |
| topic_similarity | 0.0000 | 0.0672 | 0.0366 | 0.0365 | 0.1631 |

## Field: HPI_SPENCER

### Metric: bleu_score
- Mean: 0.0003
- Std Dev: 0.0018
- Variance: 0.0000
- Shapiro-Wilk: statistic=0.1615, p=0.0000
- Kolmogorov-Smirnov: statistic=0.5385, p=0.0000
- Anderson-Darling: statistic=13.0387
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_analysis
- Mean: 0.3280
- Std Dev: 0.2198
- Variance: 0.0483
- Shapiro-Wilk: statistic=0.9453, p=0.0810
- Kolmogorov-Smirnov: statistic=0.1561, p=0.3266
- Anderson-Darling: statistic=0.5531
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_similarity
- Mean: 0.7233
- Std Dev: 0.2273
- Variance: 0.0516
- Shapiro-Wilk: statistic=0.8113, p=0.0000
- Kolmogorov-Smirnov: statistic=0.2140, p=0.0693
- Anderson-Darling: statistic=2.2792
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: rhetorical_similarity
- Mean: 0.6063
- Std Dev: 0.1990
- Variance: 0.0396
- Shapiro-Wilk: statistic=0.9036, p=0.0049
- Kolmogorov-Smirnov: statistic=0.1216, p=0.6350
- Anderson-Darling: statistic=0.7746
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: topic_similarity
- Mean: 0.1356
- Std Dev: 0.2916
- Variance: 0.0850
- Shapiro-Wilk: statistic=0.4611, p=0.0000
- Kolmogorov-Smirnov: statistic=0.4389, p=0.0000
- Anderson-Darling: statistic=8.8186
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Covariance Matrix (across metrics)

| Metric | bleu_score | content_analysis | content_similarity | rhetorical_similarity | topic_similarity |
| --- | --- | --- | --- | --- | --- |
| bleu_score | 0.0000 | -0.0000 | 0.0000 | -0.0000 | 0.0003 |
| content_analysis | -0.0000 | 0.0483 | 0.0390 | 0.0264 | 0.0023 |
| content_similarity | 0.0000 | 0.0390 | 0.0516 | 0.0348 | -0.0070 |
| rhetorical_similarity | -0.0000 | 0.0264 | 0.0348 | 0.0396 | -0.0089 |
| topic_similarity | 0.0003 | 0.0023 | -0.0070 | -0.0089 | 0.0850 |

## Field: MUSCULOSKELETAL_VERBATIM

### Metric: bleu_score
- Mean: 0.0023
- Std Dev: 0.0136
- Variance: 0.0002
- Shapiro-Wilk: statistic=0.1615, p=0.0000
- Kolmogorov-Smirnov: statistic=0.5385, p=0.0000
- Anderson-Darling: statistic=13.0387
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_analysis
- Mean: 0.3836
- Std Dev: 0.3431
- Variance: 0.1177
- Shapiro-Wilk: statistic=0.8792, p=0.0011
- Kolmogorov-Smirnov: statistic=0.2111, p=0.0758
- Anderson-Darling: statistic=1.4199
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_similarity
- Mean: 0.5863
- Std Dev: 0.3702
- Variance: 0.1371
- Shapiro-Wilk: statistic=0.8060, p=0.0000
- Kolmogorov-Smirnov: statistic=0.2297, p=0.0418
- Anderson-Darling: statistic=2.8045
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: rhetorical_similarity
- Mean: 0.5234
- Std Dev: 0.3327
- Variance: 0.1107
- Shapiro-Wilk: statistic=0.8576, p=0.0003
- Kolmogorov-Smirnov: statistic=0.1964, p=0.1172
- Anderson-Darling: statistic=2.0079
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: topic_similarity
- Mean: 0.3315
- Std Dev: 0.3725
- Variance: 0.1388
- Shapiro-Wilk: statistic=0.7656, p=0.0000
- Kolmogorov-Smirnov: statistic=0.3032, p=0.0024
- Anderson-Darling: statistic=3.3157
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Covariance Matrix (across metrics)

| Metric | bleu_score | content_analysis | content_similarity | rhetorical_similarity | topic_similarity |
| --- | --- | --- | --- | --- | --- |
| bleu_score | 0.0002 | -0.0005 | 0.0002 | 0.0005 | -0.0007 |
| content_analysis | -0.0005 | 0.1177 | 0.1105 | 0.0943 | -0.0150 |
| content_similarity | 0.0002 | 0.1105 | 0.1371 | 0.1172 | -0.0334 |
| rhetorical_similarity | 0.0005 | 0.0943 | 0.1172 | 0.1107 | -0.0333 |
| topic_similarity | -0.0007 | -0.0150 | -0.0334 | -0.0333 | 0.1388 |

## Field: IMAGING_RESULTS

### Metric: bleu_score
- Mean: 0.0152
- Std Dev: 0.0900
- Variance: 0.0081
- Shapiro-Wilk: statistic=0.1615, p=0.0000
- Kolmogorov-Smirnov: statistic=0.5385, p=0.0000
- Anderson-Darling: statistic=13.0387
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_analysis
- Mean: 0.4064
- Std Dev: 0.4201
- Variance: 0.1765
- Shapiro-Wilk: statistic=0.7728, p=0.0000
- Kolmogorov-Smirnov: statistic=0.3190, p=0.0011
- Anderson-Darling: statistic=3.3281
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_similarity
- Mean: 0.8011
- Std Dev: 0.3278
- Variance: 0.1075
- Shapiro-Wilk: statistic=0.6229, p=0.0000
- Kolmogorov-Smirnov: statistic=0.2943, p=0.0035
- Anderson-Darling: statistic=5.7838
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: rhetorical_similarity
- Mean: 0.7606
- Std Dev: 0.3136
- Variance: 0.0984
- Shapiro-Wilk: statistic=0.7197, p=0.0000
- Kolmogorov-Smirnov: statistic=0.2654, p=0.0115
- Anderson-Darling: statistic=3.6878
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: topic_similarity
- Mean: 0.3443
- Std Dev: 0.4054
- Variance: 0.1643
- Shapiro-Wilk: statistic=0.7586, p=0.0000
- Kolmogorov-Smirnov: statistic=0.2379, p=0.0315
- Anderson-Darling: statistic=3.3775
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Covariance Matrix (across metrics)

| Metric | bleu_score | content_analysis | content_similarity | rhetorical_similarity | topic_similarity |
| --- | --- | --- | --- | --- | --- |
| bleu_score | 0.0081 | 0.0071 | 0.0003 | 0.0006 | -0.0045 |
| content_analysis | 0.0071 | 0.1765 | 0.0494 | 0.0197 | 0.0610 |
| content_similarity | 0.0003 | 0.0494 | 0.1075 | 0.0901 | -0.0423 |
| rhetorical_similarity | 0.0006 | 0.0197 | 0.0901 | 0.0984 | -0.0477 |
| topic_similarity | -0.0045 | 0.0610 | -0.0423 | -0.0477 | 0.1643 |

## Field: ASSESSMENT_SPENCER

### Metric: bleu_score
- Mean: 0.1474
- Std Dev: 0.2617
- Variance: 0.0685
- Shapiro-Wilk: statistic=0.5912, p=0.0000
- Kolmogorov-Smirnov: statistic=0.4563, p=0.0000
- Anderson-Darling: statistic=7.1730
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_analysis
- Mean: 0.3271
- Std Dev: 0.2896
- Variance: 0.0839
- Shapiro-Wilk: statistic=0.9110, p=0.0079
- Kolmogorov-Smirnov: statistic=0.1563, p=0.3247
- Anderson-Darling: statistic=0.9455
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_similarity
- Mean: 0.6116
- Std Dev: 0.2554
- Variance: 0.0652
- Shapiro-Wilk: statistic=0.9564, p=0.1781
- Kolmogorov-Smirnov: statistic=0.1147, p=0.7038
- Anderson-Darling: statistic=0.5112
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: rhetorical_similarity
- Mean: 0.5482
- Std Dev: 0.2489
- Variance: 0.0619
- Shapiro-Wilk: statistic=0.9774, p=0.6731
- Kolmogorov-Smirnov: statistic=0.0697, p=0.9912
- Anderson-Darling: statistic=0.2059
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: topic_similarity
- Mean: 0.3162
- Std Dev: 0.3951
- Variance: 0.1561
- Shapiro-Wilk: statistic=0.6475, p=0.0000
- Kolmogorov-Smirnov: statistic=0.3501, p=0.0002
- Anderson-Darling: statistic=5.7584
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Covariance Matrix (across metrics)

| Metric | bleu_score | content_analysis | content_similarity | rhetorical_similarity | topic_similarity |
| --- | --- | --- | --- | --- | --- |
| bleu_score | 0.0685 | 0.0438 | 0.0325 | 0.0181 | 0.0327 |
| content_analysis | 0.0438 | 0.0839 | 0.0645 | 0.0571 | 0.0546 |
| content_similarity | 0.0325 | 0.0645 | 0.0652 | 0.0587 | 0.0374 |
| rhetorical_similarity | 0.0181 | 0.0571 | 0.0587 | 0.0619 | 0.0329 |
| topic_similarity | 0.0327 | 0.0546 | 0.0374 | 0.0329 | 0.1561 |

## Field: PLAN_SPENCER_

### Metric: bleu_score
- Mean: 0.0981
- Std Dev: 0.1713
- Variance: 0.0293
- Shapiro-Wilk: statistic=0.6402, p=0.0000
- Kolmogorov-Smirnov: statistic=0.3451, p=0.0003
- Anderson-Darling: statistic=5.6567
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_analysis
- Mean: 0.4497
- Std Dev: 0.2090
- Variance: 0.0437
- Shapiro-Wilk: statistic=0.9436, p=0.0722
- Kolmogorov-Smirnov: statistic=0.1254, p=0.5971
- Anderson-Darling: statistic=0.6490
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_similarity
- Mean: 0.7408
- Std Dev: 0.1677
- Variance: 0.0281
- Shapiro-Wilk: statistic=0.9502, p=0.1151
- Kolmogorov-Smirnov: statistic=0.0991, p=0.8482
- Anderson-Darling: statistic=0.4257
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: rhetorical_similarity
- Mean: 0.6406
- Std Dev: 0.1383
- Variance: 0.0191
- Shapiro-Wilk: statistic=0.9481, p=0.0993
- Kolmogorov-Smirnov: statistic=0.1477, p=0.3919
- Anderson-Darling: statistic=0.7287
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: topic_similarity
- Mean: 0.2153
- Std Dev: 0.3637
- Variance: 0.1323
- Shapiro-Wilk: statistic=0.5283, p=0.0000
- Kolmogorov-Smirnov: statistic=0.3981, p=0.0000
- Anderson-Darling: statistic=7.9782
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Covariance Matrix (across metrics)

| Metric | bleu_score | content_analysis | content_similarity | rhetorical_similarity | topic_similarity |
| --- | --- | --- | --- | --- | --- |
| bleu_score | 0.0293 | 0.0087 | -0.0011 | 0.0031 | 0.0156 |
| content_analysis | 0.0087 | 0.0437 | 0.0188 | 0.0154 | 0.0143 |
| content_similarity | -0.0011 | 0.0188 | 0.0281 | 0.0138 | -0.0040 |
| rhetorical_similarity | 0.0031 | 0.0154 | 0.0138 | 0.0191 | 0.0083 |
| topic_similarity | 0.0156 | 0.0143 | -0.0040 | 0.0083 | 0.1323 |


---
