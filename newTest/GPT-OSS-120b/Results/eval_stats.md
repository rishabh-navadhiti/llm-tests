# Evaluation Statistics

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
- Mean: 0.3714
- Std Dev: 0.4902
- Variance: 0.2403
- Shapiro-Wilk: statistic=0.6132, p=0.0000
- Kolmogorov-Smirnov: statistic=0.4042, p=0.0000
- Anderson-Darling: statistic=6.6846
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_similarity
- Mean: 0.8420
- Std Dev: 0.3220
- Variance: 0.1037
- Shapiro-Wilk: statistic=0.5126, p=0.0000
- Kolmogorov-Smirnov: statistic=0.4882, p=0.0000
- Anderson-Darling: statistic=8.8371
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: rhetorical_similarity
- Mean: 0.8432
- Std Dev: 0.3188
- Variance: 0.1016
- Shapiro-Wilk: statistic=0.5061, p=0.0000
- Kolmogorov-Smirnov: statistic=0.4886, p=0.0000
- Anderson-Darling: statistic=8.9520
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: topic_similarity
- Mean: 0.5131
- Std Dev: 0.4709
- Variance: 0.2217
- Shapiro-Wilk: statistic=0.7173, p=0.0000
- Kolmogorov-Smirnov: statistic=0.2907, p=0.0041
- Anderson-Darling: statistic=4.2595
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Covariance Matrix (across metrics)

| Metric | bleu_score | content_analysis | content_similarity | rhetorical_similarity | topic_similarity |
| --- | --- | --- | --- | --- | --- |
| bleu_score | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| content_analysis | 0.0000 | 0.2403 | 0.0604 | 0.0600 | 0.1862 |
| content_similarity | 0.0000 | 0.0604 | 0.1037 | 0.1025 | -0.0308 |
| rhetorical_similarity | 0.0000 | 0.0600 | 0.1025 | 0.1016 | -0.0302 |
| topic_similarity | 0.0000 | 0.1862 | -0.0308 | -0.0302 | 0.2217 |

## Field: CHIEF_COMPLAINT

### Metric: bleu_score
- Mean: 0.0941
- Std Dev: 0.2361
- Variance: 0.0557
- Shapiro-Wilk: statistic=0.4345, p=0.0000
- Kolmogorov-Smirnov: statistic=0.5121, p=0.0000
- Anderson-Darling: statistic=10.1022
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_analysis
- Mean: 0.5638
- Std Dev: 0.4085
- Variance: 0.1669
- Shapiro-Wilk: statistic=0.8202, p=0.0001
- Kolmogorov-Smirnov: statistic=0.2286, p=0.0433
- Anderson-Darling: statistic=2.2011
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_similarity
- Mean: 0.7292
- Std Dev: 0.3533
- Variance: 0.1248
- Shapiro-Wilk: statistic=0.7523, p=0.0000
- Kolmogorov-Smirnov: statistic=0.2269, p=0.0459
- Anderson-Darling: statistic=3.5762
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: rhetorical_similarity
- Mean: 0.7306
- Std Dev: 0.3445
- Variance: 0.1187
- Shapiro-Wilk: statistic=0.7722, p=0.0000
- Kolmogorov-Smirnov: statistic=0.2349, p=0.0350
- Anderson-Darling: statistic=3.2995
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: topic_similarity
- Mean: 0.6072
- Std Dev: 0.4142
- Variance: 0.1716
- Shapiro-Wilk: statistic=0.7667, p=0.0000
- Kolmogorov-Smirnov: statistic=0.3136, p=0.0015
- Anderson-Darling: statistic=3.4668
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Covariance Matrix (across metrics)

| Metric | bleu_score | content_analysis | content_similarity | rhetorical_similarity | topic_similarity |
| --- | --- | --- | --- | --- | --- |
| bleu_score | 0.0557 | 0.0328 | 0.0258 | 0.0257 | 0.0164 |
| content_analysis | 0.0328 | 0.1669 | 0.1203 | 0.1170 | 0.0963 |
| content_similarity | 0.0258 | 0.1203 | 0.1248 | 0.1205 | 0.0639 |
| rhetorical_similarity | 0.0257 | 0.1170 | 0.1205 | 0.1187 | 0.0638 |
| topic_similarity | 0.0164 | 0.0963 | 0.0639 | 0.0638 | 0.1716 |

## Field: HPI_SPENCER

### Metric: bleu_score
- Mean: 0.1493
- Std Dev: 0.1270
- Variance: 0.0161
- Shapiro-Wilk: statistic=0.8922, p=0.0025
- Kolmogorov-Smirnov: statistic=0.1373, p=0.4819
- Anderson-Darling: statistic=0.8410
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_analysis
- Mean: 0.3669
- Std Dev: 0.1786
- Variance: 0.0319
- Shapiro-Wilk: statistic=0.9903, p=0.9868
- Kolmogorov-Smirnov: statistic=0.0602, p=0.9987
- Anderson-Darling: statistic=0.1258
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_similarity
- Mean: 0.7841
- Std Dev: 0.1400
- Variance: 0.0196
- Shapiro-Wilk: statistic=0.8842, p=0.0015
- Kolmogorov-Smirnov: statistic=0.1726, p=0.2211
- Anderson-Darling: statistic=1.3062
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: rhetorical_similarity
- Mean: 0.6717
- Std Dev: 0.1271
- Variance: 0.0162
- Shapiro-Wilk: statistic=0.9626, p=0.2742
- Kolmogorov-Smirnov: statistic=0.1390, p=0.4671
- Anderson-Darling: statistic=0.5963
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: topic_similarity
- Mean: 0.3301
- Std Dev: 0.4603
- Variance: 0.2119
- Shapiro-Wilk: statistic=0.6057, p=0.0000
- Kolmogorov-Smirnov: statistic=0.3832, p=0.0000
- Anderson-Darling: statistic=6.8067
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Covariance Matrix (across metrics)

| Metric | bleu_score | content_analysis | content_similarity | rhetorical_similarity | topic_similarity |
| --- | --- | --- | --- | --- | --- |
| bleu_score | 0.0161 | 0.0127 | 0.0073 | 0.0077 | 0.0040 |
| content_analysis | 0.0127 | 0.0319 | 0.0179 | 0.0115 | 0.0086 |
| content_similarity | 0.0073 | 0.0179 | 0.0196 | 0.0123 | 0.0064 |
| rhetorical_similarity | 0.0077 | 0.0115 | 0.0123 | 0.0162 | 0.0030 |
| topic_similarity | 0.0040 | 0.0086 | 0.0064 | 0.0030 | 0.2119 |

## Field: MUSCULOSKELETAL_VERBATIM

### Metric: bleu_score
- Mean: 0.2829
- Std Dev: 0.3041
- Variance: 0.0925
- Shapiro-Wilk: statistic=0.8262, p=0.0001
- Kolmogorov-Smirnov: statistic=0.2811, p=0.0061
- Anderson-Darling: statistic=2.4937
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_analysis
- Mean: 0.3729
- Std Dev: 0.3834
- Variance: 0.1470
- Shapiro-Wilk: statistic=0.8046, p=0.0000
- Kolmogorov-Smirnov: statistic=0.2633, p=0.0125
- Anderson-Darling: statistic=2.7786
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_similarity
- Mean: 0.5252
- Std Dev: 0.3907
- Variance: 0.1526
- Shapiro-Wilk: statistic=0.7933, p=0.0000
- Kolmogorov-Smirnov: statistic=0.2419, p=0.0275
- Anderson-Darling: statistic=2.9680
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: rhetorical_similarity
- Mean: 0.5079
- Std Dev: 0.4131
- Variance: 0.1706
- Shapiro-Wilk: statistic=0.8070, p=0.0000
- Kolmogorov-Smirnov: statistic=0.2292, p=0.0424
- Anderson-Darling: statistic=2.7143
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: topic_similarity
- Mean: 0.4561
- Std Dev: 0.3791
- Variance: 0.1437
- Shapiro-Wilk: statistic=0.8235, p=0.0001
- Kolmogorov-Smirnov: statistic=0.1963, p=0.1175
- Anderson-Darling: statistic=2.3376
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Covariance Matrix (across metrics)

| Metric | bleu_score | content_analysis | content_similarity | rhetorical_similarity | topic_similarity |
| --- | --- | --- | --- | --- | --- |
| bleu_score | 0.0925 | 0.1107 | 0.1047 | 0.1119 | 0.0159 |
| content_analysis | 0.1107 | 0.1470 | 0.1361 | 0.1393 | 0.0306 |
| content_similarity | 0.1047 | 0.1361 | 0.1526 | 0.1489 | 0.0083 |
| rhetorical_similarity | 0.1119 | 0.1393 | 0.1489 | 0.1706 | 0.0027 |
| topic_similarity | 0.0159 | 0.0306 | 0.0083 | 0.0027 | 0.1437 |

## Field: IMAGING_RESULTS

### Metric: bleu_score
- Mean: 0.1639
- Std Dev: 0.3018
- Variance: 0.0911
- Shapiro-Wilk: statistic=0.6059, p=0.0000
- Kolmogorov-Smirnov: statistic=0.3637, p=0.0001
- Anderson-Darling: statistic=5.8148
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_analysis
- Mean: 0.4511
- Std Dev: 0.4088
- Variance: 0.1671
- Shapiro-Wilk: statistic=0.8114, p=0.0000
- Kolmogorov-Smirnov: statistic=0.2651, p=0.0116
- Anderson-Darling: statistic=2.5518
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_similarity
- Mean: 0.8510
- Std Dev: 0.2458
- Variance: 0.0604
- Shapiro-Wilk: statistic=0.6642, p=0.0000
- Kolmogorov-Smirnov: statistic=0.2722, p=0.0088
- Anderson-Darling: statistic=4.3427
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: rhetorical_similarity
- Mean: 0.8077
- Std Dev: 0.2752
- Variance: 0.0757
- Shapiro-Wilk: statistic=0.7345, p=0.0000
- Kolmogorov-Smirnov: statistic=0.2424, p=0.0270
- Anderson-Darling: statistic=3.3004
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: topic_similarity
- Mean: 0.3021
- Std Dev: 0.4162
- Variance: 0.1732
- Shapiro-Wilk: statistic=0.6853, p=0.0000
- Kolmogorov-Smirnov: statistic=0.3068, p=0.0020
- Anderson-Darling: statistic=4.8693
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Covariance Matrix (across metrics)

| Metric | bleu_score | content_analysis | content_similarity | rhetorical_similarity | topic_similarity |
| --- | --- | --- | --- | --- | --- |
| bleu_score | 0.0911 | 0.0638 | 0.0091 | 0.0084 | 0.0331 |
| content_analysis | 0.0638 | 0.1671 | 0.0100 | 0.0019 | 0.0828 |
| content_similarity | 0.0091 | 0.0100 | 0.0604 | 0.0651 | -0.0257 |
| rhetorical_similarity | 0.0084 | 0.0019 | 0.0651 | 0.0757 | -0.0452 |
| topic_similarity | 0.0331 | 0.0828 | -0.0257 | -0.0452 | 0.1732 |

## Field: ASSESSMENT_SPENCER

### Metric: bleu_score
- Mean: 0.0511
- Std Dev: 0.1209
- Variance: 0.0146
- Shapiro-Wilk: statistic=0.4977, p=0.0000
- Kolmogorov-Smirnov: statistic=0.4636, p=0.0000
- Anderson-Darling: statistic=7.9437
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_analysis
- Mean: 0.3283
- Std Dev: 0.2749
- Variance: 0.0756
- Shapiro-Wilk: statistic=0.9117, p=0.0083
- Kolmogorov-Smirnov: statistic=0.1170, p=0.6812
- Anderson-Darling: statistic=0.7965
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_similarity
- Mean: 0.6262
- Std Dev: 0.2004
- Variance: 0.0402
- Shapiro-Wilk: statistic=0.9656, p=0.3333
- Kolmogorov-Smirnov: statistic=0.1087, p=0.7622
- Anderson-Darling: statistic=0.4494
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: rhetorical_similarity
- Mean: 0.5375
- Std Dev: 0.1903
- Variance: 0.0362
- Shapiro-Wilk: statistic=0.9712, p=0.4781
- Kolmogorov-Smirnov: statistic=0.0991, p=0.8487
- Anderson-Darling: statistic=0.3439
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: topic_similarity
- Mean: 0.3709
- Std Dev: 0.4418
- Variance: 0.1952
- Shapiro-Wilk: statistic=0.6513, p=0.0000
- Kolmogorov-Smirnov: statistic=0.3578, p=0.0002
- Anderson-Darling: statistic=5.8018
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Covariance Matrix (across metrics)

| Metric | bleu_score | content_analysis | content_similarity | rhetorical_similarity | topic_similarity |
| --- | --- | --- | --- | --- | --- |
| bleu_score | 0.0146 | 0.0126 | 0.0074 | 0.0059 | 0.0069 |
| content_analysis | 0.0126 | 0.0756 | 0.0469 | 0.0420 | 0.0262 |
| content_similarity | 0.0074 | 0.0469 | 0.0402 | 0.0329 | 0.0164 |
| rhetorical_similarity | 0.0059 | 0.0420 | 0.0329 | 0.0362 | 0.0009 |
| topic_similarity | 0.0069 | 0.0262 | 0.0164 | 0.0009 | 0.1952 |

## Field: PLAN_SPENCER_

### Metric: bleu_score
- Mean: 0.2286
- Std Dev: 0.1965
- Variance: 0.0386
- Shapiro-Wilk: statistic=0.9232, p=0.0176
- Kolmogorov-Smirnov: statistic=0.1223, p=0.6277
- Anderson-Darling: statistic=0.6847
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_analysis
- Mean: 0.5252
- Std Dev: 0.2570
- Variance: 0.0660
- Shapiro-Wilk: statistic=0.9693, p=0.4247
- Kolmogorov-Smirnov: statistic=0.1181, p=0.6702
- Anderson-Darling: statistic=0.3735
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_similarity
- Mean: 0.7706
- Std Dev: 0.2060
- Variance: 0.0424
- Shapiro-Wilk: statistic=0.8293, p=0.0001
- Kolmogorov-Smirnov: statistic=0.1818, p=0.1745
- Anderson-Darling: statistic=1.9485
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: rhetorical_similarity
- Mean: 0.6703
- Std Dev: 0.1759
- Variance: 0.0309
- Shapiro-Wilk: statistic=0.9411, p=0.0606
- Kolmogorov-Smirnov: statistic=0.1209, p=0.6418
- Anderson-Darling: statistic=0.5366
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: topic_similarity
- Mean: 0.2728
- Std Dev: 0.4056
- Variance: 0.1645
- Shapiro-Wilk: statistic=0.5975, p=0.0000
- Kolmogorov-Smirnov: statistic=0.4067, p=0.0000
- Anderson-Darling: statistic=6.8431
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Covariance Matrix (across metrics)

| Metric | bleu_score | content_analysis | content_similarity | rhetorical_similarity | topic_similarity |
| --- | --- | --- | --- | --- | --- |
| bleu_score | 0.0386 | 0.0292 | 0.0235 | 0.0226 | -0.0218 |
| content_analysis | 0.0292 | 0.0660 | 0.0439 | 0.0262 | 0.0090 |
| content_similarity | 0.0235 | 0.0439 | 0.0424 | 0.0256 | 0.0117 |
| rhetorical_similarity | 0.0226 | 0.0262 | 0.0256 | 0.0309 | 0.0087 |
| topic_similarity | -0.0218 | 0.0090 | 0.0117 | 0.0087 | 0.1645 |


---
