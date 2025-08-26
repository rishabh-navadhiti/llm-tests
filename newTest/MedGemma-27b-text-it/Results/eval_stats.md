# Evaluation Statistics Medgemma

## Field: PATIENT_NAME

### Metric: bleu_score
- Mean: 0.0000
- Std Dev: 0.0000
- Variance: 0.0000
- Shapiro-Wilk: statistic=1.0000, p=1.0000
- Kolmogorov-Smirnov: statistic=0.5000, p=0.0000
- Anderson-Darling: statistic=nan
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_analysis
- Mean: 0.3286
- Std Dev: 0.4721
- Variance: 0.2229
- Shapiro-Wilk: statistic=0.6093, p=0.0000
- Kolmogorov-Smirnov: statistic=0.3996, p=0.0002
- Anderson-Darling: statistic=5.3588
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_similarity
- Mean: 0.6372
- Std Dev: 0.4127
- Variance: 0.1704
- Shapiro-Wilk: statistic=0.6873, p=0.0000
- Kolmogorov-Smirnov: statistic=0.3460, p=0.0017
- Anderson-Darling: statistic=4.0834
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: rhetorical_similarity
- Mean: 0.6259
- Std Dev: 0.4245
- Variance: 0.1802
- Shapiro-Wilk: statistic=0.6948, p=0.0000
- Kolmogorov-Smirnov: statistic=0.3466, p=0.0016
- Anderson-Darling: statistic=4.0656
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: topic_similarity
- Mean: 0.5989
- Std Dev: 0.3810
- Variance: 0.1452
- Shapiro-Wilk: statistic=0.8075, p=0.0001
- Kolmogorov-Smirnov: statistic=0.2165, p=0.1243
- Anderson-Darling: statistic=2.0747
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Covariance Matrix (across metrics)

| Metric | bleu_score | content_analysis | content_similarity | rhetorical_similarity | topic_similarity |
| --- | --- | --- | --- | --- | --- |
| bleu_score | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| content_analysis | 0.0000 | 0.2229 | 0.1219 | 0.1255 | 0.1308 |
| content_similarity | 0.0000 | 0.1219 | 0.1704 | 0.1744 | -0.0072 |
| rhetorical_similarity | 0.0000 | 0.1255 | 0.1744 | 0.1802 | -0.0076 |
| topic_similarity | 0.0000 | 0.1308 | -0.0072 | -0.0076 | 0.1452 |

## Field: CHIEF_COMPLAINT

### Metric: bleu_score
- Mean: 0.1071
- Std Dev: 0.3150
- Variance: 0.0992
- Shapiro-Wilk: statistic=0.3606, p=0.0000
- Kolmogorov-Smirnov: statistic=0.5260, p=0.0000
- Anderson-Darling: statistic=9.0008
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_analysis
- Mean: 0.5708
- Std Dev: 0.3955
- Variance: 0.1564
- Shapiro-Wilk: statistic=0.8436, p=0.0007
- Kolmogorov-Smirnov: statistic=0.2182, p=0.1191
- Anderson-Darling: statistic=1.4584
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_similarity
- Mean: 0.7104
- Std Dev: 0.3319
- Variance: 0.1101
- Shapiro-Wilk: statistic=0.8037, p=0.0001
- Kolmogorov-Smirnov: statistic=0.2284, p=0.0914
- Anderson-Darling: statistic=2.1703
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: rhetorical_similarity
- Mean: 0.7117
- Std Dev: 0.3262
- Variance: 0.1064
- Shapiro-Wilk: statistic=0.8036, p=0.0001
- Kolmogorov-Smirnov: statistic=0.2588, p=0.0384
- Anderson-Darling: statistic=2.1092
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: topic_similarity
- Mean: 0.5566
- Std Dev: 0.4116
- Variance: 0.1694
- Shapiro-Wilk: statistic=0.7691, p=0.0000
- Kolmogorov-Smirnov: statistic=0.2842, p=0.0171
- Anderson-Darling: statistic=2.7452
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Covariance Matrix (across metrics)

| Metric | bleu_score | content_analysis | content_similarity | rhetorical_similarity | topic_similarity |
| --- | --- | --- | --- | --- | --- |
| bleu_score | 0.0992 | 0.0477 | 0.0322 | 0.0320 | 0.0493 |
| content_analysis | 0.0477 | 0.1564 | 0.1096 | 0.1035 | 0.0665 |
| content_similarity | 0.0322 | 0.1096 | 0.1101 | 0.1065 | 0.0470 |
| rhetorical_similarity | 0.0320 | 0.1035 | 0.1065 | 0.1064 | 0.0438 |
| topic_similarity | 0.0493 | 0.0665 | 0.0470 | 0.0438 | 0.1694 |

## Field: HPI_SPENCER

### Metric: bleu_score
- Mean: 0.1134
- Std Dev: 0.1531
- Variance: 0.0234
- Shapiro-Wilk: statistic=0.7720, p=0.0000
- Kolmogorov-Smirnov: statistic=0.3063, p=0.0079
- Anderson-Darling: statistic=2.4446
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_analysis
- Mean: 0.3517
- Std Dev: 0.2166
- Variance: 0.0469
- Shapiro-Wilk: statistic=0.9668, p=0.4974
- Kolmogorov-Smirnov: statistic=0.1066, p=0.8748
- Anderson-Darling: statistic=0.2862
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_similarity
- Mean: 0.7350
- Std Dev: 0.1798
- Variance: 0.0323
- Shapiro-Wilk: statistic=0.8518, p=0.0010
- Kolmogorov-Smirnov: statistic=0.2070, p=0.1573
- Anderson-Darling: statistic=1.3442
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: rhetorical_similarity
- Mean: 0.6431
- Std Dev: 0.1819
- Variance: 0.0331
- Shapiro-Wilk: statistic=0.8788, p=0.0038
- Kolmogorov-Smirnov: statistic=0.1635, p=0.3992
- Anderson-Darling: statistic=0.9082
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: topic_similarity
- Mean: 0.2211
- Std Dev: 0.3753
- Variance: 0.1409
- Shapiro-Wilk: statistic=0.5630, p=0.0000
- Kolmogorov-Smirnov: statistic=0.3921, p=0.0002
- Anderson-Darling: statistic=5.8901
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Covariance Matrix (across metrics)

| Metric | bleu_score | content_analysis | content_similarity | rhetorical_similarity | topic_similarity |
| --- | --- | --- | --- | --- | --- |
| bleu_score | 0.0234 | 0.0156 | 0.0080 | 0.0101 | 0.0304 |
| content_analysis | 0.0156 | 0.0469 | 0.0299 | 0.0295 | 0.0403 |
| content_similarity | 0.0080 | 0.0299 | 0.0323 | 0.0280 | 0.0128 |
| rhetorical_similarity | 0.0101 | 0.0295 | 0.0280 | 0.0331 | 0.0156 |
| topic_similarity | 0.0304 | 0.0403 | 0.0128 | 0.0156 | 0.1409 |

## Field: MUSCULOSKELETAL_VERBATIM

### Metric: bleu_score
- Mean: 0.0786
- Std Dev: 0.1701
- Variance: 0.0289
- Shapiro-Wilk: statistic=0.5312, p=0.0000
- Kolmogorov-Smirnov: statistic=0.4499, p=0.0000
- Anderson-Darling: statistic=6.2731
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_analysis
- Mean: 0.1774
- Std Dev: 0.2126
- Variance: 0.0452
- Shapiro-Wilk: statistic=0.8191, p=0.0002
- Kolmogorov-Smirnov: statistic=0.2622, p=0.0346
- Anderson-Darling: statistic=1.9234
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_similarity
- Mean: 0.5277
- Std Dev: 0.2941
- Variance: 0.0865
- Shapiro-Wilk: statistic=0.8476, p=0.0008
- Kolmogorov-Smirnov: statistic=0.2358, p=0.0747
- Anderson-Darling: statistic=1.7809
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: rhetorical_similarity
- Mean: 0.3633
- Std Dev: 0.3237
- Variance: 0.1047
- Shapiro-Wilk: statistic=0.8181, p=0.0002
- Kolmogorov-Smirnov: statistic=0.2338, p=0.0789
- Anderson-Darling: statistic=2.0277
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: topic_similarity
- Mean: 0.2808
- Std Dev: 0.3590
- Variance: 0.1289
- Shapiro-Wilk: statistic=0.7404, p=0.0000
- Kolmogorov-Smirnov: statistic=0.3108, p=0.0067
- Anderson-Darling: statistic=3.0247
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Covariance Matrix (across metrics)

| Metric | bleu_score | content_analysis | content_similarity | rhetorical_similarity | topic_similarity |
| --- | --- | --- | --- | --- | --- |
| bleu_score | 0.0289 | 0.0225 | 0.0184 | 0.0284 | 0.0068 |
| content_analysis | 0.0225 | 0.0452 | 0.0370 | 0.0562 | -0.0035 |
| content_similarity | 0.0184 | 0.0370 | 0.0865 | 0.0549 | -0.0487 |
| rhetorical_similarity | 0.0284 | 0.0562 | 0.0549 | 0.1047 | -0.0145 |
| topic_similarity | 0.0068 | -0.0035 | -0.0487 | -0.0145 | 0.1289 |

## Field: IMAGING_RESULTS

### Metric: bleu_score
- Mean: 0.0112
- Std Dev: 0.0502
- Variance: 0.0025
- Shapiro-Wilk: statistic=0.2375, p=0.0000
- Kolmogorov-Smirnov: statistic=0.5166, p=0.0000
- Anderson-Darling: statistic=9.3757
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_analysis
- Mean: 0.2314
- Std Dev: 0.2993
- Variance: 0.0896
- Shapiro-Wilk: statistic=0.7803, p=0.0000
- Kolmogorov-Smirnov: statistic=0.3160, p=0.0055
- Anderson-Darling: statistic=2.5767
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_similarity
- Mean: 0.5701
- Std Dev: 0.2867
- Variance: 0.0822
- Shapiro-Wilk: statistic=0.8395, p=0.0006
- Kolmogorov-Smirnov: statistic=0.3184, p=0.0050
- Anderson-Darling: statistic=2.1708
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: rhetorical_similarity
- Mean: 0.2925
- Std Dev: 0.3205
- Variance: 0.1027
- Shapiro-Wilk: statistic=0.8348, p=0.0005
- Kolmogorov-Smirnov: statistic=0.2256, p=0.0984
- Anderson-Darling: statistic=1.8358
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: topic_similarity
- Mean: 0.2758
- Std Dev: 0.3289
- Variance: 0.1082
- Shapiro-Wilk: statistic=0.8047, p=0.0001
- Kolmogorov-Smirnov: statistic=0.2029, p=0.1733
- Anderson-Darling: statistic=1.9952
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Covariance Matrix (across metrics)

| Metric | bleu_score | content_analysis | content_similarity | rhetorical_similarity | topic_similarity |
| --- | --- | --- | --- | --- | --- |
| bleu_score | 0.0025 | 0.0031 | 0.0017 | 0.0042 | -0.0015 |
| content_analysis | 0.0031 | 0.0896 | 0.0392 | 0.0683 | 0.0148 |
| content_similarity | 0.0017 | 0.0392 | 0.0822 | 0.0517 | -0.0497 |
| rhetorical_similarity | 0.0042 | 0.0683 | 0.0517 | 0.1027 | -0.0061 |
| topic_similarity | -0.0015 | 0.0148 | -0.0497 | -0.0061 | 0.1082 |

## Field: ASSESSMENT_SPENCER

### Metric: bleu_score
- Mean: 0.0713
- Std Dev: 0.2018
- Variance: 0.0407
- Shapiro-Wilk: statistic=0.4040, p=0.0000
- Kolmogorov-Smirnov: statistic=0.4952, p=0.0000
- Anderson-Darling: statistic=7.8048
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_analysis
- Mean: 0.2896
- Std Dev: 0.3194
- Variance: 0.1020
- Shapiro-Wilk: statistic=0.8140, p=0.0002
- Kolmogorov-Smirnov: statistic=0.2013, p=0.1801
- Anderson-Darling: statistic=1.7899
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_similarity
- Mean: 0.5674
- Std Dev: 0.2440
- Variance: 0.0596
- Shapiro-Wilk: statistic=0.9763, p=0.7557
- Kolmogorov-Smirnov: statistic=0.0679, p=0.9984
- Anderson-Darling: statistic=0.1825
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: rhetorical_similarity
- Mean: 0.5029
- Std Dev: 0.2476
- Variance: 0.0613
- Shapiro-Wilk: statistic=0.9613, p=0.3739
- Kolmogorov-Smirnov: statistic=0.1463, p=0.5384
- Anderson-Darling: statistic=0.4694
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: topic_similarity
- Mean: 0.2392
- Std Dev: 0.3370
- Variance: 0.1136
- Shapiro-Wilk: statistic=0.6161, p=0.0000
- Kolmogorov-Smirnov: statistic=0.3561, p=0.0011
- Anderson-Darling: statistic=4.8237
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Covariance Matrix (across metrics)

| Metric | bleu_score | content_analysis | content_similarity | rhetorical_similarity | topic_similarity |
| --- | --- | --- | --- | --- | --- |
| bleu_score | 0.0407 | 0.0312 | 0.0188 | 0.0181 | 0.0232 |
| content_analysis | 0.0312 | 0.1020 | 0.0642 | 0.0638 | 0.0246 |
| content_similarity | 0.0188 | 0.0642 | 0.0596 | 0.0570 | 0.0159 |
| rhetorical_similarity | 0.0181 | 0.0638 | 0.0570 | 0.0613 | 0.0217 |
| topic_similarity | 0.0232 | 0.0246 | 0.0159 | 0.0217 | 0.1136 |

## Field: PLAN_SPENCER_

### Metric: bleu_score
- Mean: 0.1507
- Std Dev: 0.2108
- Variance: 0.0445
- Shapiro-Wilk: statistic=0.7492, p=0.0000
- Kolmogorov-Smirnov: statistic=0.2984, p=0.0105
- Anderson-Darling: statistic=2.8961
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_analysis
- Mean: 0.3139
- Std Dev: 0.2588
- Variance: 0.0670
- Shapiro-Wilk: statistic=0.9072, p=0.0169
- Kolmogorov-Smirnov: statistic=0.1439, p=0.5598
- Anderson-Darling: statistic=0.8867
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_similarity
- Mean: 0.5936
- Std Dev: 0.2456
- Variance: 0.0603
- Shapiro-Wilk: statistic=0.9688, p=0.5481
- Kolmogorov-Smirnov: statistic=0.0705, p=0.9973
- Anderson-Darling: statistic=0.2306
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: rhetorical_similarity
- Mean: 0.5337
- Std Dev: 0.2157
- Variance: 0.0465
- Shapiro-Wilk: statistic=0.9377, p=0.0966
- Kolmogorov-Smirnov: statistic=0.1402, p=0.5917
- Anderson-Darling: statistic=0.6644
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: topic_similarity
- Mean: 0.3612
- Std Dev: 0.4267
- Variance: 0.1821
- Shapiro-Wilk: statistic=0.6813, p=0.0000
- Kolmogorov-Smirnov: statistic=0.3312, p=0.0031
- Anderson-Darling: statistic=4.0736
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Covariance Matrix (across metrics)

| Metric | bleu_score | content_analysis | content_similarity | rhetorical_similarity | topic_similarity |
| --- | --- | --- | --- | --- | --- |
| bleu_score | 0.0445 | 0.0381 | 0.0279 | 0.0272 | 0.0161 |
| content_analysis | 0.0381 | 0.0670 | 0.0514 | 0.0445 | 0.0253 |
| content_similarity | 0.0279 | 0.0514 | 0.0603 | 0.0478 | 0.0061 |
| rhetorical_similarity | 0.0272 | 0.0445 | 0.0478 | 0.0465 | 0.0146 |
| topic_similarity | 0.0161 | 0.0253 | 0.0061 | 0.0146 | 0.1821 |


---
