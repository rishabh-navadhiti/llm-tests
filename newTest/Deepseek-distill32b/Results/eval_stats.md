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
- Mean: 0.3976
- Std Dev: 0.4675
- Variance: 0.2186
- Shapiro-Wilk: statistic=0.6893, p=0.0000
- Kolmogorov-Smirnov: statistic=0.3453, p=0.0003
- Anderson-Darling: statistic=4.9182
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_similarity
- Mean: 0.8820
- Std Dev: 0.2593
- Variance: 0.0672
- Shapiro-Wilk: statistic=0.5110, p=0.0000
- Kolmogorov-Smirnov: statistic=0.4184, p=0.0000
- Anderson-Darling: statistic=8.1763
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: rhetorical_similarity
- Mean: 0.8775
- Std Dev: 0.2595
- Variance: 0.0673
- Shapiro-Wilk: statistic=0.5265, p=0.0000
- Kolmogorov-Smirnov: statistic=0.4244, p=0.0000
- Anderson-Darling: statistic=7.7937
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: topic_similarity
- Mean: 0.4890
- Std Dev: 0.4773
- Variance: 0.2278
- Shapiro-Wilk: statistic=0.7068, p=0.0000
- Kolmogorov-Smirnov: statistic=0.2817, p=0.0060
- Anderson-Darling: statistic=4.4946
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Covariance Matrix (across metrics)

| Metric | bleu_score | content_analysis | content_similarity | rhetorical_similarity | topic_similarity |
| --- | --- | --- | --- | --- | --- |
| bleu_score | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| content_analysis | 0.0000 | 0.2186 | 0.0363 | 0.0350 | 0.1783 |
| content_similarity | 0.0000 | 0.0363 | 0.0672 | 0.0671 | -0.0237 |
| rhetorical_similarity | 0.0000 | 0.0350 | 0.0671 | 0.0673 | -0.0258 |
| topic_similarity | 0.0000 | 0.1783 | -0.0237 | -0.0258 | 0.2278 |

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
- Mean: 0.0000
- Std Dev: 0.0000
- Variance: 0.0000
- Shapiro-Wilk: statistic=1.0000, p=1.0000
- Kolmogorov-Smirnov: statistic=0.5000, p=0.0000
- Anderson-Darling: statistic=nan
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_analysis
- Mean: 0.3773
- Std Dev: 0.2463
- Variance: 0.0607
- Shapiro-Wilk: statistic=0.9654, p=0.3305
- Kolmogorov-Smirnov: statistic=0.1140, p=0.7109
- Anderson-Darling: statistic=0.3431
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_similarity
- Mean: 0.7446
- Std Dev: 0.2376
- Variance: 0.0565
- Shapiro-Wilk: statistic=0.7964, p=0.0000
- Kolmogorov-Smirnov: statistic=0.2131, p=0.0713
- Anderson-Darling: statistic=2.4310
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: rhetorical_similarity
- Mean: 0.6428
- Std Dev: 0.1944
- Variance: 0.0378
- Shapiro-Wilk: statistic=0.8119, p=0.0000
- Kolmogorov-Smirnov: statistic=0.2189, p=0.0594
- Anderson-Darling: statistic=2.1560
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: topic_similarity
- Mean: 0.1919
- Std Dev: 0.3534
- Variance: 0.1249
- Shapiro-Wilk: statistic=0.5312, p=0.0000
- Kolmogorov-Smirnov: statistic=0.4291, p=0.0000
- Anderson-Darling: statistic=7.9211
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Covariance Matrix (across metrics)

| Metric | bleu_score | content_analysis | content_similarity | rhetorical_similarity | topic_similarity |
| --- | --- | --- | --- | --- | --- |
| bleu_score | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| content_analysis | 0.0000 | 0.0607 | 0.0455 | 0.0304 | 0.0094 |
| content_similarity | 0.0000 | 0.0455 | 0.0565 | 0.0394 | -0.0023 |
| rhetorical_similarity | 0.0000 | 0.0304 | 0.0394 | 0.0378 | -0.0100 |
| topic_similarity | 0.0000 | 0.0094 | -0.0023 | -0.0100 | 0.1249 |

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
- Mean: 0.3335
- Std Dev: 0.3756
- Variance: 0.1411
- Shapiro-Wilk: statistic=0.8034, p=0.0000
- Kolmogorov-Smirnov: statistic=0.2698, p=0.0097
- Anderson-Darling: statistic=2.6939
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_similarity
- Mean: 0.5035
- Std Dev: 0.4048
- Variance: 0.1639
- Shapiro-Wilk: statistic=0.8210, p=0.0001
- Kolmogorov-Smirnov: statistic=0.2240, p=0.0503
- Anderson-Darling: statistic=2.4510
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: rhetorical_similarity
- Mean: 0.4591
- Std Dev: 0.3751
- Variance: 0.1407
- Shapiro-Wilk: statistic=0.8439, p=0.0002
- Kolmogorov-Smirnov: statistic=0.2465, p=0.0234
- Anderson-Darling: statistic=2.0611
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: topic_similarity
- Mean: 0.4952
- Std Dev: 0.3786
- Variance: 0.1433
- Shapiro-Wilk: statistic=0.8319, p=0.0001
- Kolmogorov-Smirnov: statistic=0.1933, p=0.1279
- Anderson-Darling: statistic=2.1523
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Covariance Matrix (across metrics)

| Metric | bleu_score | content_analysis | content_similarity | rhetorical_similarity | topic_similarity |
| --- | --- | --- | --- | --- | --- |
| bleu_score | 0.0002 | -0.0004 | 0.0004 | 0.0006 | -0.0011 |
| content_analysis | -0.0004 | 0.1411 | 0.1362 | 0.1214 | 0.0208 |
| content_similarity | 0.0004 | 0.1362 | 0.1639 | 0.1459 | 0.0104 |
| rhetorical_similarity | 0.0006 | 0.1214 | 0.1459 | 0.1407 | 0.0160 |
| topic_similarity | -0.0011 | 0.0208 | 0.0104 | 0.0160 | 0.1433 |

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
- Mean: 0.4277
- Std Dev: 0.4244
- Variance: 0.1801
- Shapiro-Wilk: statistic=0.7837, p=0.0000
- Kolmogorov-Smirnov: statistic=0.3003, p=0.0027
- Anderson-Darling: statistic=3.0288
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_similarity
- Mean: 0.8131
- Std Dev: 0.3203
- Variance: 0.1026
- Shapiro-Wilk: statistic=0.6076, p=0.0000
- Kolmogorov-Smirnov: statistic=0.2928, p=0.0037
- Anderson-Darling: statistic=5.9516
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: rhetorical_similarity
- Mean: 0.7729
- Std Dev: 0.3060
- Variance: 0.0937
- Shapiro-Wilk: statistic=0.7138, p=0.0000
- Kolmogorov-Smirnov: statistic=0.2512, p=0.0197
- Anderson-Darling: statistic=3.6212
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: topic_similarity
- Mean: 0.2937
- Std Dev: 0.3753
- Variance: 0.1408
- Shapiro-Wilk: statistic=0.7493, p=0.0000
- Kolmogorov-Smirnov: statistic=0.2614, p=0.0134
- Anderson-Darling: statistic=3.5007
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Covariance Matrix (across metrics)

| Metric | bleu_score | content_analysis | content_similarity | rhetorical_similarity | topic_similarity |
| --- | --- | --- | --- | --- | --- |
| bleu_score | 0.0081 | 0.0067 | 0.0001 | 0.0004 | -0.0037 |
| content_analysis | 0.0067 | 0.1801 | 0.0459 | 0.0148 | 0.0755 |
| content_similarity | 0.0001 | 0.0459 | 0.1026 | 0.0850 | -0.0309 |
| rhetorical_similarity | 0.0004 | 0.0148 | 0.0850 | 0.0937 | -0.0363 |
| topic_similarity | -0.0037 | 0.0755 | -0.0309 | -0.0363 | 0.1408 |

## Field: ASSESSMENT_SPENCER

### Metric: bleu_score
- Mean: 0.1550
- Std Dev: 0.2611
- Variance: 0.0682
- Shapiro-Wilk: statistic=0.6215, p=0.0000
- Kolmogorov-Smirnov: statistic=0.4378, p=0.0000
- Anderson-Darling: statistic=6.4946
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_analysis
- Mean: 0.3150
- Std Dev: 0.2901
- Variance: 0.0842
- Shapiro-Wilk: statistic=0.9049, p=0.0054
- Kolmogorov-Smirnov: statistic=0.1469, p=0.3981
- Anderson-Darling: statistic=0.9999
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_similarity
- Mean: 0.6103
- Std Dev: 0.2236
- Variance: 0.0500
- Shapiro-Wilk: statistic=0.9749, p=0.5902
- Kolmogorov-Smirnov: statistic=0.1023, p=0.8217
- Anderson-Darling: statistic=0.2697
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: rhetorical_similarity
- Mean: 0.5194
- Std Dev: 0.2113
- Variance: 0.0446
- Shapiro-Wilk: statistic=0.9745, p=0.5790
- Kolmogorov-Smirnov: statistic=0.0997, p=0.8433
- Anderson-Darling: statistic=0.3969
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: topic_similarity
- Mean: 0.2425
- Std Dev: 0.3620
- Variance: 0.1310
- Shapiro-Wilk: statistic=0.5632, p=0.0000
- Kolmogorov-Smirnov: statistic=0.4009, p=0.0000
- Anderson-Darling: statistic=7.3408
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Covariance Matrix (across metrics)

| Metric | bleu_score | content_analysis | content_similarity | rhetorical_similarity | topic_similarity |
| --- | --- | --- | --- | --- | --- |
| bleu_score | 0.0682 | 0.0462 | 0.0337 | 0.0227 | 0.0422 |
| content_analysis | 0.0462 | 0.0842 | 0.0571 | 0.0503 | 0.0575 |
| content_similarity | 0.0337 | 0.0571 | 0.0500 | 0.0428 | 0.0350 |
| rhetorical_similarity | 0.0227 | 0.0503 | 0.0428 | 0.0446 | 0.0318 |
| topic_similarity | 0.0422 | 0.0575 | 0.0350 | 0.0318 | 0.1310 |

## Field: PLAN_SPENCER_

### Metric: bleu_score
- Mean: 0.1144
- Std Dev: 0.2122
- Variance: 0.0450
- Shapiro-Wilk: statistic=0.6147, p=0.0000
- Kolmogorov-Smirnov: statistic=0.3622, p=0.0001
- Anderson-Darling: statistic=5.8680
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_analysis
- Mean: 0.4639
- Std Dev: 0.2346
- Variance: 0.0550
- Shapiro-Wilk: statistic=0.9608, p=0.2416
- Kolmogorov-Smirnov: statistic=0.1111, p=0.7394
- Anderson-Darling: statistic=0.4196
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: content_similarity
- Mean: 0.7719
- Std Dev: 0.1884
- Variance: 0.0355
- Shapiro-Wilk: statistic=0.8793, p=0.0012
- Kolmogorov-Smirnov: statistic=0.1482, p=0.3873
- Anderson-Darling: statistic=1.3012
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: rhetorical_similarity
- Mean: 0.6461
- Std Dev: 0.1681
- Variance: 0.0282
- Shapiro-Wilk: statistic=0.9671, p=0.3695
- Kolmogorov-Smirnov: statistic=0.1288, p=0.5628
- Anderson-Darling: statistic=0.5100
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Metric: topic_similarity
- Mean: 0.2458
- Std Dev: 0.3840
- Variance: 0.1475
- Shapiro-Wilk: statistic=0.5590, p=0.0000
- Kolmogorov-Smirnov: statistic=0.3969, p=0.0000
- Anderson-Darling: statistic=7.4960
  - Critical Values: 0.5270, 0.6000, 0.7190, 0.8390, 0.9980
  - Significance Levels: 15.0, 10.0, 5.0, 2.5, 1.0

### Covariance Matrix (across metrics)

| Metric | bleu_score | content_analysis | content_similarity | rhetorical_similarity | topic_similarity |
| --- | --- | --- | --- | --- | --- |
| bleu_score | 0.0450 | 0.0280 | 0.0082 | 0.0087 | 0.0030 |
| content_analysis | 0.0280 | 0.0550 | 0.0282 | 0.0261 | 0.0278 |
| content_similarity | 0.0082 | 0.0282 | 0.0355 | 0.0218 | 0.0146 |
| rhetorical_similarity | 0.0087 | 0.0261 | 0.0218 | 0.0282 | 0.0290 |
| topic_similarity | 0.0030 | 0.0278 | 0.0146 | 0.0290 | 0.1475 |


---
