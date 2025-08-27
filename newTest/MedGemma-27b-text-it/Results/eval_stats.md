# Evaluation Statistics

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
- Mean: 0.3571
- Std Dev: 0.4880
- Variance: 0.2381
- Shapiro-Wilk: statistic=0.6083, p=0.0000
- Kolmogorov-Smirnov: statistic=0.4107, p=0.0001
- Anderson-Darling: statistic=5.4219
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_similarity
- Mean: 0.8444
- Std Dev: 0.3176
- Variance: 0.1008
- Shapiro-Wilk: statistic=0.5268, p=0.0000
- Kolmogorov-Smirnov: statistic=0.4736, p=0.0000
- Anderson-Darling: statistic=6.6837
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: rhetorical_similarity
- Mean: 0.8202
- Std Dev: 0.3527
- Variance: 0.1244
- Shapiro-Wilk: statistic=0.5350, p=0.0000
- Kolmogorov-Smirnov: statistic=0.4806, p=0.0000
- Anderson-Darling: statistic=6.7455
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: topic_similarity
- Mean: 0.4913
- Std Dev: 0.4819
- Variance: 0.2323
- Shapiro-Wilk: statistic=0.7005, p=0.0000
- Kolmogorov-Smirnov: statistic=0.3103, p=0.0068
- Anderson-Darling: statistic=3.6989
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Covariance Matrix (across metrics)

| Metric | bleu_score | content_analysis | content_similarity | rhetorical_similarity | topic_similarity |
| --- | --- | --- | --- | --- | --- |
| bleu_score | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| content_analysis | 0.0000 | 0.2381 | 0.0576 | 0.0666 | 0.1884 |
| content_similarity | 0.0000 | 0.0576 | 0.1008 | 0.1037 | -0.0326 |
| rhetorical_similarity | 0.0000 | 0.0666 | 0.1037 | 0.1244 | -0.0198 |
| topic_similarity | 0.0000 | 0.1884 | -0.0326 | -0.0198 | 0.2323 |

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
- Mean: 0.1286
- Std Dev: 0.1653
- Variance: 0.0273
- Shapiro-Wilk: statistic=0.7814, p=0.0001
- Kolmogorov-Smirnov: statistic=0.3175, p=0.0052
- Anderson-Darling: statistic=2.5215
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_analysis
- Mean: 0.3687
- Std Dev: 0.2339
- Variance: 0.0547
- Shapiro-Wilk: statistic=0.9511, p=0.2108
- Kolmogorov-Smirnov: statistic=0.1413, p=0.5821
- Anderson-Darling: statistic=0.5387
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_similarity
- Mean: 0.7644
- Std Dev: 0.1930
- Variance: 0.0372
- Shapiro-Wilk: statistic=0.8384, p=0.0006
- Kolmogorov-Smirnov: statistic=0.1894, p=0.2359
- Anderson-Darling: statistic=1.3682
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: rhetorical_similarity
- Mean: 0.6799
- Std Dev: 0.1893
- Variance: 0.0358
- Shapiro-Wilk: statistic=0.8455, p=0.0008
- Kolmogorov-Smirnov: statistic=0.2001, p=0.1850
- Anderson-Darling: statistic=1.1094
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: topic_similarity
- Mean: 0.2914
- Std Dev: 0.4214
- Variance: 0.1775
- Shapiro-Wilk: statistic=0.6192, p=0.0000
- Kolmogorov-Smirnov: statistic=0.3670, p=0.0007
- Anderson-Darling: statistic=5.0996
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Covariance Matrix (across metrics)

| Metric | bleu_score | content_analysis | content_similarity | rhetorical_similarity | topic_similarity |
| --- | --- | --- | --- | --- | --- |
| bleu_score | 0.0273 | 0.0195 | 0.0101 | 0.0110 | 0.0296 |
| content_analysis | 0.0195 | 0.0547 | 0.0342 | 0.0304 | 0.0405 |
| content_similarity | 0.0101 | 0.0342 | 0.0372 | 0.0322 | 0.0149 |
| rhetorical_similarity | 0.0110 | 0.0304 | 0.0322 | 0.0358 | 0.0192 |
| topic_similarity | 0.0296 | 0.0405 | 0.0149 | 0.0192 | 0.1775 |

## Field: MUSCULOSKELETAL_VERBATIM

### Metric: bleu_score
- Mean: 0.0305
- Std Dev: 0.1004
- Variance: 0.0101
- Shapiro-Wilk: statistic=0.3527, p=0.0000
- Kolmogorov-Smirnov: statistic=0.4875, p=0.0000
- Anderson-Darling: statistic=8.2499
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_analysis
- Mean: 0.1281
- Std Dev: 0.1892
- Variance: 0.0358
- Shapiro-Wilk: statistic=0.7251, p=0.0000
- Kolmogorov-Smirnov: statistic=0.3223, p=0.0043
- Anderson-Darling: statistic=2.9868
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_similarity
- Mean: 0.4583
- Std Dev: 0.3073
- Variance: 0.0944
- Shapiro-Wilk: statistic=0.8702, p=0.0025
- Kolmogorov-Smirnov: statistic=0.2087, p=0.1510
- Anderson-Darling: statistic=1.4791
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: rhetorical_similarity
- Mean: 0.2869
- Std Dev: 0.2992
- Variance: 0.0895
- Shapiro-Wilk: statistic=0.8310, p=0.0004
- Kolmogorov-Smirnov: statistic=0.2503, p=0.0494
- Anderson-Darling: statistic=1.8273
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: topic_similarity
- Mean: 0.3143
- Std Dev: 0.3553
- Variance: 0.1262
- Shapiro-Wilk: statistic=0.7928, p=0.0001
- Kolmogorov-Smirnov: statistic=0.2745, p=0.0235
- Anderson-Darling: statistic=2.2527
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Covariance Matrix (across metrics)

| Metric | bleu_score | content_analysis | content_similarity | rhetorical_similarity | topic_similarity |
| --- | --- | --- | --- | --- | --- |
| bleu_score | 0.0101 | 0.0080 | 0.0089 | 0.0138 | 0.0081 |
| content_analysis | 0.0080 | 0.0358 | 0.0334 | 0.0442 | -0.0044 |
| content_similarity | 0.0089 | 0.0334 | 0.0944 | 0.0499 | -0.0489 |
| rhetorical_similarity | 0.0138 | 0.0442 | 0.0499 | 0.0895 | -0.0087 |
| topic_similarity | 0.0081 | -0.0044 | -0.0489 | -0.0087 | 0.1262 |

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
- Mean: 0.2685
- Std Dev: 0.3271
- Variance: 0.1070
- Shapiro-Wilk: statistic=0.7952, p=0.0001
- Kolmogorov-Smirnov: statistic=0.2941, p=0.0122
- Anderson-Darling: statistic=2.2769
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_similarity
- Mean: 0.5923
- Std Dev: 0.2904
- Variance: 0.0844
- Shapiro-Wilk: statistic=0.8350, p=0.0005
- Kolmogorov-Smirnov: statistic=0.2883, p=0.0149
- Anderson-Darling: statistic=2.1712
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: rhetorical_similarity
- Mean: 0.3068
- Std Dev: 0.3327
- Variance: 0.1107
- Shapiro-Wilk: statistic=0.8416, p=0.0006
- Kolmogorov-Smirnov: statistic=0.2307, p=0.0857
- Anderson-Darling: statistic=1.7393
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: topic_similarity
- Mean: 0.3059
- Std Dev: 0.3522
- Variance: 0.1241
- Shapiro-Wilk: statistic=0.8085, p=0.0002
- Kolmogorov-Smirnov: statistic=0.2359, p=0.0745
- Anderson-Darling: statistic=1.9740
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Covariance Matrix (across metrics)

| Metric | bleu_score | content_analysis | content_similarity | rhetorical_similarity | topic_similarity |
| --- | --- | --- | --- | --- | --- |
| bleu_score | 0.0025 | 0.0027 | 0.0014 | 0.0040 | -0.0019 |
| content_analysis | 0.0027 | 0.1070 | 0.0457 | 0.0801 | 0.0492 |
| content_similarity | 0.0014 | 0.0457 | 0.0844 | 0.0584 | -0.0349 |
| rhetorical_similarity | 0.0040 | 0.0801 | 0.0584 | 0.1107 | 0.0135 |
| topic_similarity | -0.0019 | 0.0492 | -0.0349 | 0.0135 | 0.1241 |

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
- Mean: 0.2583
- Std Dev: 0.2889
- Variance: 0.0835
- Shapiro-Wilk: statistic=0.8140, p=0.0002
- Kolmogorov-Smirnov: statistic=0.2257, p=0.0981
- Anderson-Darling: statistic=1.7330
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_similarity
- Mean: 0.5604
- Std Dev: 0.2274
- Variance: 0.0517
- Shapiro-Wilk: statistic=0.9782, p=0.8051
- Kolmogorov-Smirnov: statistic=0.0770, p=0.9919
- Anderson-Darling: statistic=0.1987
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: rhetorical_similarity
- Mean: 0.4738
- Std Dev: 0.2192
- Variance: 0.0480
- Shapiro-Wilk: statistic=0.9474, p=0.1702
- Kolmogorov-Smirnov: statistic=0.1578, p=0.4428
- Anderson-Darling: statistic=0.6974
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: topic_similarity
- Mean: 0.1983
- Std Dev: 0.3062
- Variance: 0.0938
- Shapiro-Wilk: statistic=0.5689, p=0.0000
- Kolmogorov-Smirnov: statistic=0.3989, p=0.0002
- Anderson-Darling: statistic=5.3647
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Covariance Matrix (across metrics)

| Metric | bleu_score | content_analysis | content_similarity | rhetorical_similarity | topic_similarity |
| --- | --- | --- | --- | --- | --- |
| bleu_score | 0.0407 | 0.0335 | 0.0193 | 0.0202 | 0.0262 |
| content_analysis | 0.0335 | 0.0835 | 0.0554 | 0.0514 | 0.0245 |
| content_similarity | 0.0193 | 0.0554 | 0.0517 | 0.0459 | 0.0096 |
| rhetorical_similarity | 0.0202 | 0.0514 | 0.0459 | 0.0480 | 0.0189 |
| topic_similarity | 0.0262 | 0.0245 | 0.0096 | 0.0189 | 0.0938 |

## Field: PLAN_SPENCER_

### Metric: bleu_score
- Mean: 0.1680
- Std Dev: 0.2102
- Variance: 0.0442
- Shapiro-Wilk: statistic=0.7959, p=0.0001
- Kolmogorov-Smirnov: statistic=0.2878, p=0.0151
- Anderson-Darling: statistic=2.2608
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_analysis
- Mean: 0.3117
- Std Dev: 0.2581
- Variance: 0.0666
- Shapiro-Wilk: statistic=0.9051, p=0.0151
- Kolmogorov-Smirnov: statistic=0.1470, p=0.5324
- Anderson-Darling: statistic=0.9045
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_similarity
- Mean: 0.6273
- Std Dev: 0.2405
- Variance: 0.0579
- Shapiro-Wilk: statistic=0.9470, p=0.1661
- Kolmogorov-Smirnov: statistic=0.1196, p=0.7747
- Anderson-Darling: statistic=0.4313
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: rhetorical_similarity
- Mean: 0.5492
- Std Dev: 0.2271
- Variance: 0.0516
- Shapiro-Wilk: statistic=0.9445, p=0.1437
- Kolmogorov-Smirnov: statistic=0.1493, p=0.5126
- Anderson-Darling: statistic=0.5624
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: topic_similarity
- Mean: 0.3637
- Std Dev: 0.4251
- Variance: 0.1807
- Shapiro-Wilk: statistic=0.6863, p=0.0000
- Kolmogorov-Smirnov: statistic=0.3339, p=0.0028
- Anderson-Darling: statistic=3.9859
  - Critical Values: 0.5180, 0.5900, 0.7080, 0.8260, 0.9830
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Covariance Matrix (across metrics)

| Metric | bleu_score | content_analysis | content_similarity | rhetorical_similarity | topic_similarity |
| --- | --- | --- | --- | --- | --- |
| bleu_score | 0.0442 | 0.0397 | 0.0274 | 0.0305 | 0.0282 |
| content_analysis | 0.0397 | 0.0666 | 0.0477 | 0.0451 | 0.0227 |
| content_similarity | 0.0274 | 0.0477 | 0.0579 | 0.0489 | 0.0131 |
| rhetorical_similarity | 0.0305 | 0.0451 | 0.0489 | 0.0516 | 0.0133 |
| topic_similarity | 0.0282 | 0.0227 | 0.0131 | 0.0133 | 0.1807 |


---
