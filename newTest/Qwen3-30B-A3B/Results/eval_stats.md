# Evaluation Statistics

## Field: PATIENT_NAME

### Metric: bleu_score
- Mean: 0.0000
- Std Dev: 0.0000
- Variance: 0.0000
- Shapiro-Wilk: statistic=1.0000, p=1.0000
- Kolmogorov-Smirnov: statistic=0.5000, p=0.0000
- Anderson-Darling: statistic=nan
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_analysis
- Mean: 0.3258
- Std Dev: 0.4697
- Variance: 0.2206
- Shapiro-Wilk: statistic=0.6071, p=0.0000
- Kolmogorov-Smirnov: statistic=0.4227, p=0.0000
- Anderson-Darling: statistic=6.4090
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_similarity
- Mean: 0.8556
- Std Dev: 0.3068
- Variance: 0.0941
- Shapiro-Wilk: statistic=0.4936, p=0.0000
- Kolmogorov-Smirnov: statistic=0.4690, p=0.0000
- Anderson-Darling: statistic=8.5427
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: rhetorical_similarity
- Mean: 0.8499
- Std Dev: 0.3125
- Variance: 0.0977
- Shapiro-Wilk: statistic=0.5023, p=0.0000
- Kolmogorov-Smirnov: statistic=0.4724, p=0.0000
- Anderson-Darling: statistic=8.3242
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: topic_similarity
- Mean: 0.4668
- Std Dev: 0.4761
- Variance: 0.2267
- Shapiro-Wilk: statistic=0.7043, p=0.0000
- Kolmogorov-Smirnov: statistic=0.3214, p=0.0016
- Anderson-Darling: statistic=4.2956
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Covariance Matrix (across metrics)

| Metric | bleu_score | content_analysis | content_similarity | rhetorical_similarity | topic_similarity |
| --- | --- | --- | --- | --- | --- |
| bleu_score | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| content_analysis | 0.0000 | 0.2206 | 0.0470 | 0.0467 | 0.1791 |
| content_similarity | 0.0000 | 0.0470 | 0.0941 | 0.0957 | -0.0394 |
| rhetorical_similarity | 0.0000 | 0.0467 | 0.0957 | 0.0977 | -0.0421 |
| topic_similarity | 0.0000 | 0.1791 | -0.0394 | -0.0421 | 0.2267 |

## Field: CHIEF_COMPLAINT

### Metric: bleu_score
- Mean: 0.1918
- Std Dev: 0.3434
- Variance: 0.1179
- Shapiro-Wilk: statistic=0.6062, p=0.0000
- Kolmogorov-Smirnov: statistic=0.4390, p=0.0000
- Anderson-Darling: statistic=6.2142
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_analysis
- Mean: 0.5744
- Std Dev: 0.3710
- Variance: 0.1376
- Shapiro-Wilk: statistic=0.8721, p=0.0011
- Kolmogorov-Smirnov: statistic=0.2077, p=0.1001
- Anderson-Darling: statistic=1.3307
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_similarity
- Mean: 0.7537
- Std Dev: 0.3284
- Variance: 0.1078
- Shapiro-Wilk: statistic=0.7459, p=0.0000
- Kolmogorov-Smirnov: statistic=0.2266, p=0.0569
- Anderson-Darling: statistic=3.1222
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: rhetorical_similarity
- Mean: 0.7588
- Std Dev: 0.2987
- Variance: 0.0892
- Shapiro-Wilk: statistic=0.7758, p=0.0000
- Kolmogorov-Smirnov: statistic=0.2097, p=0.0945
- Anderson-Darling: statistic=2.6022
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: topic_similarity
- Mean: 0.6649
- Std Dev: 0.4092
- Variance: 0.1675
- Shapiro-Wilk: statistic=0.7043, p=0.0000
- Kolmogorov-Smirnov: statistic=0.3646, p=0.0002
- Anderson-Darling: statistic=4.4740
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Covariance Matrix (across metrics)

| Metric | bleu_score | content_analysis | content_similarity | rhetorical_similarity | topic_similarity |
| --- | --- | --- | --- | --- | --- |
| bleu_score | 0.1179 | 0.0704 | 0.0450 | 0.0423 | 0.0443 |
| content_analysis | 0.0704 | 0.1376 | 0.1029 | 0.0921 | 0.0756 |
| content_similarity | 0.0450 | 0.1029 | 0.1078 | 0.0964 | 0.0578 |
| rhetorical_similarity | 0.0423 | 0.0921 | 0.0964 | 0.0892 | 0.0497 |
| topic_similarity | 0.0443 | 0.0756 | 0.0578 | 0.0497 | 0.1675 |

## Field: HPI_SPENCER

### Metric: bleu_score
- Mean: 0.2140
- Std Dev: 0.1759
- Variance: 0.0310
- Shapiro-Wilk: statistic=0.9139, p=0.0125
- Kolmogorov-Smirnov: statistic=0.1431, p=0.4657
- Anderson-Darling: statistic=0.9383
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_analysis
- Mean: 0.3649
- Std Dev: 0.2147
- Variance: 0.0461
- Shapiro-Wilk: statistic=0.9787, p=0.7471
- Kolmogorov-Smirnov: statistic=0.0979, p=0.8793
- Anderson-Darling: statistic=0.2249
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_similarity
- Mean: 0.7481
- Std Dev: 0.1999
- Variance: 0.0400
- Shapiro-Wilk: statistic=0.8693, p=0.0009
- Kolmogorov-Smirnov: statistic=0.1457, p=0.4438
- Anderson-Darling: statistic=1.2287
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: rhetorical_similarity
- Mean: 0.7173
- Std Dev: 0.1637
- Variance: 0.0268
- Shapiro-Wilk: statistic=0.8357, p=0.0002
- Kolmogorov-Smirnov: statistic=0.1952, p=0.1411
- Anderson-Darling: statistic=1.4776
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: topic_similarity
- Mean: 0.2667
- Std Dev: 0.4183
- Variance: 0.1749
- Shapiro-Wilk: statistic=0.5939, p=0.0000
- Kolmogorov-Smirnov: statistic=0.4173, p=0.0000
- Anderson-Darling: statistic=6.5744
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Covariance Matrix (across metrics)

| Metric | bleu_score | content_analysis | content_similarity | rhetorical_similarity | topic_similarity |
| --- | --- | --- | --- | --- | --- |
| bleu_score | 0.0310 | 0.0316 | 0.0198 | 0.0175 | 0.0168 |
| content_analysis | 0.0316 | 0.0461 | 0.0315 | 0.0233 | 0.0193 |
| content_similarity | 0.0198 | 0.0315 | 0.0400 | 0.0276 | 0.0006 |
| rhetorical_similarity | 0.0175 | 0.0233 | 0.0276 | 0.0268 | -0.0045 |
| topic_similarity | 0.0168 | 0.0193 | 0.0006 | -0.0045 | 0.1749 |

## Field: MUSCULOSKELETAL_VERBATIM

### Metric: bleu_score
- Mean: 0.3049
- Std Dev: 0.3270
- Variance: 0.1070
- Shapiro-Wilk: statistic=0.8145, p=0.0001
- Kolmogorov-Smirnov: statistic=0.2789, p=0.0092
- Anderson-Darling: statistic=2.4437
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_analysis
- Mean: 0.4063
- Std Dev: 0.4170
- Variance: 0.1739
- Shapiro-Wilk: statistic=0.7848, p=0.0000
- Kolmogorov-Smirnov: statistic=0.2896, p=0.0060
- Anderson-Darling: statistic=2.8629
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_similarity
- Mean: 0.5400
- Std Dev: 0.3868
- Variance: 0.1496
- Shapiro-Wilk: statistic=0.8253, p=0.0001
- Kolmogorov-Smirnov: statistic=0.2130, p=0.0858
- Anderson-Darling: statistic=2.2114
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: rhetorical_similarity
- Mean: 0.5268
- Std Dev: 0.3768
- Variance: 0.1420
- Shapiro-Wilk: statistic=0.8526, p=0.0004
- Kolmogorov-Smirnov: statistic=0.1673, p=0.2814
- Anderson-Darling: statistic=1.7946
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: topic_similarity
- Mean: 0.4543
- Std Dev: 0.3835
- Variance: 0.1471
- Shapiro-Wilk: statistic=0.8273, p=0.0001
- Kolmogorov-Smirnov: statistic=0.2037, p=0.1120
- Anderson-Darling: statistic=2.1145
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Covariance Matrix (across metrics)

| Metric | bleu_score | content_analysis | content_similarity | rhetorical_similarity | topic_similarity |
| --- | --- | --- | --- | --- | --- |
| bleu_score | 0.1070 | 0.1312 | 0.1126 | 0.1124 | 0.0378 |
| content_analysis | 0.1312 | 0.1739 | 0.1499 | 0.1449 | 0.0540 |
| content_similarity | 0.1126 | 0.1499 | 0.1496 | 0.1331 | 0.0292 |
| rhetorical_similarity | 0.1124 | 0.1449 | 0.1331 | 0.1420 | 0.0269 |
| topic_similarity | 0.0378 | 0.0540 | 0.0292 | 0.0269 | 0.1471 |

## Field: IMAGING_RESULTS

### Metric: bleu_score
- Mean: 0.1594
- Std Dev: 0.2652
- Variance: 0.0703
- Shapiro-Wilk: statistic=0.6743, p=0.0000
- Kolmogorov-Smirnov: statistic=0.3625, p=0.0002
- Anderson-Darling: statistic=4.4679
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_analysis
- Mean: 0.5028
- Std Dev: 0.4184
- Variance: 0.1751
- Shapiro-Wilk: statistic=0.8080, p=0.0000
- Kolmogorov-Smirnov: statistic=0.2489, p=0.0275
- Anderson-Darling: statistic=2.3655
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_similarity
- Mean: 0.9084
- Std Dev: 0.1279
- Variance: 0.0164
- Shapiro-Wilk: statistic=0.7536, p=0.0000
- Kolmogorov-Smirnov: statistic=0.2370, p=0.0409
- Anderson-Darling: statistic=3.2593
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: rhetorical_similarity
- Mean: 0.8700
- Std Dev: 0.1736
- Variance: 0.0301
- Shapiro-Wilk: statistic=0.7755, p=0.0000
- Kolmogorov-Smirnov: statistic=0.2474, p=0.0290
- Anderson-Darling: statistic=2.8515
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: topic_similarity
- Mean: 0.3183
- Std Dev: 0.4319
- Variance: 0.1866
- Shapiro-Wilk: statistic=0.6672, p=0.0000
- Kolmogorov-Smirnov: statistic=0.2741, p=0.0111
- Anderson-Darling: statistic=4.9586
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Covariance Matrix (across metrics)

| Metric | bleu_score | content_analysis | content_similarity | rhetorical_similarity | topic_similarity |
| --- | --- | --- | --- | --- | --- |
| bleu_score | 0.0703 | 0.0594 | 0.0037 | 0.0029 | 0.0395 |
| content_analysis | 0.0594 | 0.1751 | -0.0049 | -0.0080 | 0.0954 |
| content_similarity | 0.0037 | -0.0049 | 0.0164 | 0.0215 | -0.0081 |
| rhetorical_similarity | 0.0029 | -0.0080 | 0.0215 | 0.0301 | -0.0150 |
| topic_similarity | 0.0395 | 0.0954 | -0.0081 | -0.0150 | 0.1866 |

## Field: ASSESSMENT_SPENCER

### Metric: bleu_score
- Mean: 0.0652
- Std Dev: 0.1636
- Variance: 0.0268
- Shapiro-Wilk: statistic=0.4679, p=0.0000
- Kolmogorov-Smirnov: statistic=0.4730, p=0.0000
- Anderson-Darling: statistic=7.8286
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_analysis
- Mean: 0.3184
- Std Dev: 0.2433
- Variance: 0.0592
- Shapiro-Wilk: statistic=0.9246, p=0.0245
- Kolmogorov-Smirnov: statistic=0.1458, p=0.4428
- Anderson-Darling: statistic=0.8166
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_similarity
- Mean: 0.6167
- Std Dev: 0.2111
- Variance: 0.0445
- Shapiro-Wilk: statistic=0.9162, p=0.0144
- Kolmogorov-Smirnov: statistic=0.1445, p=0.4543
- Anderson-Darling: statistic=0.7369
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: rhetorical_similarity
- Mean: 0.5269
- Std Dev: 0.1898
- Variance: 0.0360
- Shapiro-Wilk: statistic=0.9300, p=0.0351
- Kolmogorov-Smirnov: statistic=0.1442, p=0.4561
- Anderson-Darling: statistic=0.8243
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: topic_similarity
- Mean: 0.2226
- Std Dev: 0.3522
- Variance: 0.1241
- Shapiro-Wilk: statistic=0.5716, p=0.0000
- Kolmogorov-Smirnov: statistic=0.4008, p=0.0000
- Anderson-Darling: statistic=6.6479
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Covariance Matrix (across metrics)

| Metric | bleu_score | content_analysis | content_similarity | rhetorical_similarity | topic_similarity |
| --- | --- | --- | --- | --- | --- |
| bleu_score | 0.0268 | 0.0177 | 0.0101 | 0.0045 | 0.0069 |
| content_analysis | 0.0177 | 0.0592 | 0.0427 | 0.0346 | 0.0125 |
| content_similarity | 0.0101 | 0.0427 | 0.0445 | 0.0370 | 0.0097 |
| rhetorical_similarity | 0.0045 | 0.0346 | 0.0370 | 0.0360 | 0.0122 |
| topic_similarity | 0.0069 | 0.0125 | 0.0097 | 0.0122 | 0.1241 |

## Field: PLAN_SPENCER_

### Metric: bleu_score
- Mean: 0.3618
- Std Dev: 0.2277
- Variance: 0.0519
- Shapiro-Wilk: statistic=0.9709, p=0.5048
- Kolmogorov-Smirnov: statistic=0.0721, p=0.9905
- Anderson-Darling: statistic=0.2122
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_analysis
- Mean: 0.5678
- Std Dev: 0.2168
- Variance: 0.0470
- Shapiro-Wilk: statistic=0.9701, p=0.4818
- Kolmogorov-Smirnov: statistic=0.1153, p=0.7294
- Anderson-Darling: statistic=0.3893
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_similarity
- Mean: 0.8455
- Std Dev: 0.1537
- Variance: 0.0236
- Shapiro-Wilk: statistic=0.7882, p=0.0000
- Kolmogorov-Smirnov: statistic=0.2234, p=0.0629
- Anderson-Darling: statistic=2.6507
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: rhetorical_similarity
- Mean: 0.7554
- Std Dev: 0.1512
- Variance: 0.0229
- Shapiro-Wilk: statistic=0.9131, p=0.0119
- Kolmogorov-Smirnov: statistic=0.1705, p=0.2613
- Anderson-Darling: statistic=0.8965
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: topic_similarity
- Mean: 0.3642
- Std Dev: 0.4492
- Variance: 0.2018
- Shapiro-Wilk: statistic=0.6406, p=0.0000
- Kolmogorov-Smirnov: statistic=0.3726, p=0.0001
- Anderson-Darling: statistic=5.7078
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Covariance Matrix (across metrics)

| Metric | bleu_score | content_analysis | content_similarity | rhetorical_similarity | topic_similarity |
| --- | --- | --- | --- | --- | --- |
| bleu_score | 0.0519 | 0.0426 | 0.0215 | 0.0254 | 0.0098 |
| content_analysis | 0.0426 | 0.0470 | 0.0239 | 0.0257 | 0.0074 |
| content_similarity | 0.0215 | 0.0239 | 0.0236 | 0.0185 | 0.0247 |
| rhetorical_similarity | 0.0254 | 0.0257 | 0.0185 | 0.0229 | 0.0282 |
| topic_similarity | 0.0098 | 0.0074 | 0.0247 | 0.0282 | 0.2018 |


---
