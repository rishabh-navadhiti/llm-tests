# Evaluation Statistics Qwen

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
- Mean: 0.2409
- Std Dev: 0.4216
- Variance: 0.1777
- Shapiro-Wilk: statistic=0.5623, p=0.0000
- Kolmogorov-Smirnov: statistic=0.4434, p=0.0000
- Anderson-Darling: statistic=7.2194
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_similarity
- Mean: 0.5587
- Std Dev: 0.4026
- Variance: 0.1621
- Shapiro-Wilk: statistic=0.7196, p=0.0000
- Kolmogorov-Smirnov: statistic=0.2683, p=0.0138
- Anderson-Darling: statistic=4.0957
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: rhetorical_similarity
- Mean: 0.5483
- Std Dev: 0.4017
- Variance: 0.1614
- Shapiro-Wilk: statistic=0.7209, p=0.0000
- Kolmogorov-Smirnov: statistic=0.2765, p=0.0101
- Anderson-Darling: statistic=4.0730
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: topic_similarity
- Mean: 0.5813
- Std Dev: 0.3582
- Variance: 0.1283
- Shapiro-Wilk: statistic=0.8345, p=0.0002
- Kolmogorov-Smirnov: statistic=0.2492, p=0.0272
- Anderson-Darling: statistic=2.1099
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Covariance Matrix (across metrics)

| Metric | bleu_score | content_analysis | content_similarity | rhetorical_similarity | topic_similarity |
| --- | --- | --- | --- | --- | --- |
| bleu_score | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| content_analysis | 0.0000 | 0.1777 | 0.1066 | 0.1068 | 0.0990 |
| content_similarity | 0.0000 | 0.1066 | 0.1621 | 0.1611 | -0.0137 |
| rhetorical_similarity | 0.0000 | 0.1068 | 0.1611 | 0.1614 | -0.0139 |
| topic_similarity | 0.0000 | 0.0990 | -0.0137 | -0.0139 | 0.1283 |

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
- Mean: 0.2079
- Std Dev: 0.1719
- Variance: 0.0295
- Shapiro-Wilk: statistic=0.9088, p=0.0091
- Kolmogorov-Smirnov: statistic=0.1132, p=0.7498
- Anderson-Darling: statistic=0.8865
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_analysis
- Mean: 0.3391
- Std Dev: 0.1978
- Variance: 0.0391
- Shapiro-Wilk: statistic=0.9718, p=0.5319
- Kolmogorov-Smirnov: statistic=0.0874, p=0.9435
- Anderson-Darling: statistic=0.2449
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_similarity
- Mean: 0.7325
- Std Dev: 0.1898
- Variance: 0.0360
- Shapiro-Wilk: statistic=0.8697, p=0.0010
- Kolmogorov-Smirnov: statistic=0.1915, p=0.1557
- Anderson-Darling: statistic=1.3239
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: rhetorical_similarity
- Mean: 0.6907
- Std Dev: 0.1631
- Variance: 0.0266
- Shapiro-Wilk: statistic=0.8839, p=0.0021
- Kolmogorov-Smirnov: statistic=0.1184, p=0.7004
- Anderson-Darling: statistic=0.8427
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: topic_similarity
- Mean: 0.2422
- Std Dev: 0.4085
- Variance: 0.1669
- Shapiro-Wilk: statistic=0.5608, p=0.0000
- Kolmogorov-Smirnov: statistic=0.4304, p=0.0000
- Anderson-Darling: statistic=7.1898
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Covariance Matrix (across metrics)

| Metric | bleu_score | content_analysis | content_similarity | rhetorical_similarity | topic_similarity |
| --- | --- | --- | --- | --- | --- |
| bleu_score | 0.0295 | 0.0270 | 0.0170 | 0.0187 | -0.0108 |
| content_analysis | 0.0270 | 0.0391 | 0.0276 | 0.0212 | -0.0011 |
| content_similarity | 0.0170 | 0.0276 | 0.0360 | 0.0236 | -0.0039 |
| rhetorical_similarity | 0.0187 | 0.0212 | 0.0236 | 0.0266 | -0.0147 |
| topic_similarity | -0.0108 | -0.0011 | -0.0039 | -0.0147 | 0.1669 |

## Field: MUSCULOSKELETAL_VERBATIM

### Metric: bleu_score
- Mean: 0.2688
- Std Dev: 0.2565
- Variance: 0.0658
- Shapiro-Wilk: statistic=0.8872, p=0.0025
- Kolmogorov-Smirnov: statistic=0.1860, p=0.1795
- Anderson-Darling: statistic=1.2317
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_analysis
- Mean: 0.3924
- Std Dev: 0.3392
- Variance: 0.1151
- Shapiro-Wilk: statistic=0.8991, p=0.0050
- Kolmogorov-Smirnov: statistic=0.1794, p=0.2116
- Anderson-Darling: statistic=1.0061
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_similarity
- Mean: 0.5968
- Std Dev: 0.3279
- Variance: 0.1075
- Shapiro-Wilk: statistic=0.8666, p=0.0008
- Kolmogorov-Smirnov: statistic=0.1887, p=0.1673
- Anderson-Darling: statistic=1.6556
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: rhetorical_similarity
- Mean: 0.5622
- Std Dev: 0.3234
- Variance: 0.1046
- Shapiro-Wilk: statistic=0.8891, p=0.0028
- Kolmogorov-Smirnov: statistic=0.1865, p=0.1771
- Anderson-Darling: statistic=1.3722
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: topic_similarity
- Mean: 0.4001
- Std Dev: 0.4132
- Variance: 0.1707
- Shapiro-Wilk: statistic=0.7696, p=0.0000
- Kolmogorov-Smirnov: statistic=0.2707, p=0.0126
- Anderson-Darling: statistic=3.0369
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Covariance Matrix (across metrics)

| Metric | bleu_score | content_analysis | content_similarity | rhetorical_similarity | topic_similarity |
| --- | --- | --- | --- | --- | --- |
| bleu_score | 0.0658 | 0.0766 | 0.0651 | 0.0687 | 0.0044 |
| content_analysis | 0.0766 | 0.1151 | 0.0959 | 0.0937 | -0.0019 |
| content_similarity | 0.0651 | 0.0959 | 0.1075 | 0.0935 | 0.0030 |
| rhetorical_similarity | 0.0687 | 0.0937 | 0.0935 | 0.1046 | 0.0035 |
| topic_similarity | 0.0044 | -0.0019 | 0.0030 | 0.0035 | 0.1707 |

## Field: IMAGING_RESULTS

### Metric: bleu_score
- Mean: 0.1559
- Std Dev: 0.2653
- Variance: 0.0704
- Shapiro-Wilk: statistic=0.6595, p=0.0000
- Kolmogorov-Smirnov: statistic=0.3882, p=0.0001
- Anderson-Darling: statistic=4.7779
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_analysis
- Mean: 0.4595
- Std Dev: 0.4122
- Variance: 0.1699
- Shapiro-Wilk: statistic=0.8155, p=0.0001
- Kolmogorov-Smirnov: statistic=0.2615, p=0.0177
- Anderson-Darling: statistic=2.2545
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_similarity
- Mean: 0.8918
- Std Dev: 0.1546
- Variance: 0.0239
- Shapiro-Wilk: statistic=0.7375, p=0.0000
- Kolmogorov-Smirnov: statistic=0.2419, p=0.0348
- Anderson-Darling: statistic=2.9325
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: rhetorical_similarity
- Mean: 0.8501
- Std Dev: 0.1971
- Variance: 0.0388
- Shapiro-Wilk: statistic=0.7827, p=0.0000
- Kolmogorov-Smirnov: statistic=0.2259, p=0.0582
- Anderson-Darling: statistic=2.5674
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: topic_similarity
- Mean: 0.2968
- Std Dev: 0.4139
- Variance: 0.1713
- Shapiro-Wilk: statistic=0.6687, p=0.0000
- Kolmogorov-Smirnov: statistic=0.2725, p=0.0118
- Anderson-Darling: statistic=4.8477
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Covariance Matrix (across metrics)

| Metric | bleu_score | content_analysis | content_similarity | rhetorical_similarity | topic_similarity |
| --- | --- | --- | --- | --- | --- |
| bleu_score | 0.0704 | 0.0623 | 0.0061 | 0.0058 | 0.0416 |
| content_analysis | 0.0623 | 0.1699 | 0.0019 | -0.0001 | 0.0755 |
| content_similarity | 0.0061 | 0.0019 | 0.0239 | 0.0293 | -0.0151 |
| rhetorical_similarity | 0.0058 | -0.0001 | 0.0293 | 0.0388 | -0.0232 |
| topic_similarity | 0.0416 | 0.0755 | -0.0151 | -0.0232 | 0.1713 |

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
- Mean: 0.3406
- Std Dev: 0.2463
- Variance: 0.0607
- Shapiro-Wilk: statistic=0.9350, p=0.0486
- Kolmogorov-Smirnov: statistic=0.1287, p=0.5996
- Anderson-Darling: statistic=0.6593
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_similarity
- Mean: 0.6196
- Std Dev: 0.2451
- Variance: 0.0601
- Shapiro-Wilk: statistic=0.8914, p=0.0032
- Kolmogorov-Smirnov: statistic=0.1816, p=0.2005
- Anderson-Darling: statistic=1.1078
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: rhetorical_similarity
- Mean: 0.5504
- Std Dev: 0.2337
- Variance: 0.0546
- Shapiro-Wilk: statistic=0.9262, p=0.0272
- Kolmogorov-Smirnov: statistic=0.1081, p=0.7963
- Anderson-Darling: statistic=0.6568
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: topic_similarity
- Mean: 0.2430
- Std Dev: 0.3501
- Variance: 0.1226
- Shapiro-Wilk: statistic=0.6232, p=0.0000
- Kolmogorov-Smirnov: statistic=0.3630, p=0.0002
- Anderson-Darling: statistic=5.6262
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Covariance Matrix (across metrics)

| Metric | bleu_score | content_analysis | content_similarity | rhetorical_similarity | topic_similarity |
| --- | --- | --- | --- | --- | --- |
| bleu_score | 0.0268 | 0.0162 | 0.0099 | 0.0029 | 0.0055 |
| content_analysis | 0.0162 | 0.0607 | 0.0502 | 0.0421 | 0.0060 |
| content_similarity | 0.0099 | 0.0502 | 0.0601 | 0.0541 | 0.0047 |
| rhetorical_similarity | 0.0029 | 0.0421 | 0.0541 | 0.0546 | 0.0087 |
| topic_similarity | 0.0055 | 0.0060 | 0.0047 | 0.0087 | 0.1226 |

## Field: PLAN_SPENCER_

### Metric: bleu_score
- Mean: 0.3359
- Std Dev: 0.2090
- Variance: 0.0437
- Shapiro-Wilk: statistic=0.9700, p=0.4804
- Kolmogorov-Smirnov: statistic=0.0872, p=0.9446
- Anderson-Darling: statistic=0.2758
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_analysis
- Mean: 0.5399
- Std Dev: 0.1983
- Variance: 0.0393
- Shapiro-Wilk: statistic=0.9749, p=0.6265
- Kolmogorov-Smirnov: statistic=0.1173, p=0.7105
- Anderson-Darling: statistic=0.3664
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_similarity
- Mean: 0.8099
- Std Dev: 0.1597
- Variance: 0.0255
- Shapiro-Wilk: statistic=0.8759, p=0.0013
- Kolmogorov-Smirnov: statistic=0.1624, p=0.3141
- Anderson-Darling: statistic=1.5086
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: rhetorical_similarity
- Mean: 0.7124
- Std Dev: 0.1511
- Variance: 0.0228
- Shapiro-Wilk: statistic=0.9781, p=0.7289
- Kolmogorov-Smirnov: statistic=0.0986, p=0.8747
- Anderson-Darling: statistic=0.2513
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: topic_similarity
- Mean: 0.3511
- Std Dev: 0.4482
- Variance: 0.2009
- Shapiro-Wilk: statistic=0.6361, p=0.0000
- Kolmogorov-Smirnov: statistic=0.3731, p=0.0001
- Anderson-Darling: statistic=5.7843
  - Critical Values: 0.5240, 0.5970, 0.7170, 0.8360, 0.9940
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Covariance Matrix (across metrics)

| Metric | bleu_score | content_analysis | content_similarity | rhetorical_similarity | topic_similarity |
| --- | --- | --- | --- | --- | --- |
| bleu_score | 0.0437 | 0.0256 | 0.0140 | 0.0180 | 0.0051 |
| content_analysis | 0.0256 | 0.0393 | 0.0254 | 0.0207 | 0.0120 |
| content_similarity | 0.0140 | 0.0254 | 0.0255 | 0.0162 | 0.0106 |
| rhetorical_similarity | 0.0180 | 0.0207 | 0.0162 | 0.0228 | 0.0091 |
| topic_similarity | 0.0051 | 0.0120 | 0.0106 | 0.0091 | 0.2009 |


---
