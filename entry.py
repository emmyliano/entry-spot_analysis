import statistics
from collections import Counter

# Vertically formatted string of numbers
numbers_str = """
6408.959
6409.579
6409.51
6409.29
6409.43
6409.512
6410.393
6410.753
6410.964
6411.108
6410.925
6410.607
6410.372
6410.635
6410.552
6410.374
6410.637
6410.652
6410.92
6410.766
6411.061
6411.061
6411.42
6411.651
6412.249
6411.917
6411.916
6412.068
6412.253
6412.948
6413.021
6412.946
6413.02
6413.366
6413.368
6413.703
6413.9
6413.829
6413.755
6413.515
6413.987
6413.601
6413.036
6413.074
6412.503
6412.922
6413.057
6412.993
6413.423
6413.336
6413.106
6413.148
6413.598
6413.167
6413.451
6413.776
6414.132
6414.151
6414.269
6414.587
6414.682
6414.483
6414.694
6414.35
6414.633
6414.708
6414.9
6414.981
6414.528
6415.104
6414.91
6414.979
6415.333
6408.883
6408.279
6408.667
6408.608
6408.562
6408.623
6408.481
6408.843
6408.601
6408.674
6408.417
6408.863
6409.142
6408.748
6408.392
6408.404
6408.433
6408.393
6407.944
6408.093
6408.054
6408.188
6407.828
6407.875
6407.924
6407.96
6408.854
6409.127
6409.225
6408.557
6408.196
6408.107
6407.967
6408.213
6408.023
6407.553
6407.94
6407.823
6407.881
6407.148
6407.126
6407.059
6406.952
6407.407
6407.931
6408.345
6408.207
6408.334
6408.862
6409.167
6408.848
6408.405
6407.994
6407.762
6407.503
6407.258
6407.405
6407.068
6406.614
6406.703
6406.014
6405.615
6406.136
6405.583
6405.595
6405.232
6405.344
6405.827
6406.258
6406.528
6406.816
6406.349
6405.853
6405.886
6405.927
6405.645
6405.338
6405.499
6405.3
6405.395
6405.65
6405.792
6406.553
6406.545
6406.687
6406.876
6407.343
6407.667
6407.965
6407.905
6408.193
6408.346
6408.421
6408.23
6400.771
6400.603
6400.417
6400.381
6400.254
6400.637
6400.727
6400.613
6401.162
6401.293
6401.17
6401.466
6401.965
6401.803
6401.728
6401.803
6401.414
6401.114
6401.13
6402.185
6402.46
6402.328
6402.297
6402.213
6401.912
6402.263
6402.334
6402.496
6402.403
6402.418
6402.112
6402.396
6402.355
6402.487
6402.317
6402.083
6401.776
6401.473
6400.922
6400.37
6400.348
6400.475
6400.557
6400.199
6400.47
6400.279
6400.364
6400.534
6400.749
6401.438
6402.027
6402.339
6402.266
6403.047
6402.897
6403.461
6403.487
6403.438
6404.119
6404.286
6404.531
6404.368
6403.961
6403.668
6404.135
6404.542
6404.659
6404.832
6404.846
6405.312
6405.347
6405.05
6405.667
6405.698
6405.988
6405.593
6405.679
6406.049
6406.404
6406.362
6406.164
6406.378
6406.632
6406.548
6406.659
6406.213
6406.722
6406.841
6407.161
6406.892
6407.727
6407.248
6407.145
6407.183
6406.81
6407.333
6407.339
6407.379
6407.65
6407.639
6408.045
6407.766
6407.657
6407.775
6407.703
6408.377
6408.702
6409.157
6409.107
6409.59
6409.81
6409.85
6409.789
6409.7
6410.162
6410.252
6410.058
6409.954
6400.35
6399.607
6399.281
6399.247
6398.902
6398.726
6399.629
6400.254
6400.386
6400.689
6400.687
6401.064
6401.27
6401.621
6401.537
6400.991
6400.623
6400.209
6400.447
6401.009
6401.578
6401.662
6401.633
6401.446
6401.468
6401.483
6401.35
6401.12
6401.075
6400.997
6400.864
6400.269
6400.304
6400.631
6401.25
6401.6
6401.504
6401.918
6401.706
6402
6401.738
6401.155
6400.964
6400.922
6400.609
6400.385
6400.519
6400.466
6400.558
6400.454
6400.715
6401.629
6401.834
6401.93
6401.647
6401.622
6401.974
6401.72
6402.237
6402.181
6402.465
6402.069
6402.262
6402.38
6401.868
6401.364
6401.195
6401.609
6401.39
6400.775
6400.592
6400.762
6401.117
6401.142
6400.48
6400.564
6400.542
6400.886
6400.834
6402.343
6402.394
6402.826
6402.817
6403.231
6402.864
6401.972
6402.281
6402.361
6402.428
6402.685
6402.681
6402.554
6402.713
6403.068
6402.562
6402.464
6401.936
6402.341
6402.546
6403.26
6403.494
6403.285
6402.953
6402.729
6402.63
6402.306
6401.943
6402.706
6402.603
6403.104
6402.677
6402.251
6402.563
6402.612
6402.619
6403.178
6402.771
6402.401
6401.574
6401.197
6400.914
6400.684
6399.984
6399.618
6399.253
6399.195
6399.29
6399.34
6399.347
6399.433
6399.694
6399.727
6399.85
6400.27
6400.493
6400.185
6400.314
6400.225
6399.946
6399.91
6400.116
6400.215
6399.921
6399.497
6400.432
6400.528
6400.527
6400.915
6401.112
6401.013
6400.703
6401.161
6402.355
6401.806
6402.044
6402.588
6402.812
6402.977
6403.247
6403.317
6403.15
6403.233
6403.097
6403.24
6402.941
6403.174
6403.28
6402.549
6402.779
6402.214
6401.628
6401.688
6402.365
6402.419
6402.88
6402.876
6403.188
6402.627
6402.537
6402.634
6402.252
6401.968
6401.773
6402.273
6402.364
6402.375
6401.946
6401.804
6402.176
6402.283
6402.379
6402.785
6403.167
6403.165
6403.374
6403.069
6403.012
6403.635
6403.549
6403.793
6404.158
6403.865
6403.647
6404.266
6404.001
6403.74
6404.693
6404.507
6404.904
6405.141
6405.666
6405.568
6405.586
6405.437
6405.416
6405.425
6404.768
6404.737
6404.933
6405.536
6405.458
6405.681
6405.764
6405.828
6405.331
6405.225
6404.979
6405.088
6404.834
6404.407
6404.622
6404.84
6404.898
6404.884
6404.251
6404.727
6403.745
6403.608
6404.179
6404.345
6404.562
6404.416
6404.45
6404.324
6403.939
6404.098
6403.99
6403.26
6403.023
6402.833
6402.753
6400.746
6400.713
6400.438
6400.538
6400.24
6400
6399.592
6399.52
6400.115
6399.989
6400.361
6399.967
6399.743
6399.738
6400.177
6399.878
6400.025
6400.139
6400.671
6400.814
6401.132
6401.216
6401.067
6400.948
6400.962
6400.212
6400.143
6400.403
6400.011
6400.251
6400.266
6400.362
6400.12
6400.243
6399.931
6399.533
6399.109
6399.263
6398.813
6399.022
6399.119
6399.665
6399.548
6399.159
6399.549
6399.282
6399.573
6399.339
6399.177
6382.794
6383.527
6383.698
6383.597
6383.997
6384.154
6384.166
6384.36
6384.455
6385.582
6386.127
6386.268
6386.25
6386.869
6386.608
6386.669
6386.527
6386.618
6386.365
6386.13
6386.445
6386.701
6386.971
6386.891
6387.162
6386.744
6386.549
6386.712
6386.901
6387.046
6386.881
6386.869
6387.395
6387.547
6387.543
6387.795
6387.607
6387.258
6387.746
6387.398
6387.864
6387.796
6387.26
6387.694
6387.088
6386.971
6387.051
6386.756
6386.21
6386.292
6386.617
6387.085
6387.631
6387.437
6386.995
6387.23
6387.089
6386.923
6386.782
6386.759
6387.24
6387.293
6387.493
6387.548
6387.462
6388.022
6388.063
6388.014
6388.44
6387.949
6387.659
6387.886
6387.327
6387.667
6387.992
6387.994
6387.868
6388.14
6388.13
6387.95
6387.951
6388.006
6387.995
6387.791
6387.908
6388.209
6389.212
6389.237
6389.335
6389.481
6389.83
6390.731
6390.75
6391.188
6390.788
6390.959
6390.711
6390.642
6390.446
6389.622
6388.83
6389.374
6389.368
6388.906
6388.556
6388.432
6388.552
6388.078
6387.863
6388.505
6388.9
6388.442
6388.333
6388.347
6388.436
6388.286
6388.597
6388.729
6388.587
6388.882
6388.877
6389.118
6388.936
6388.383
6388.107
6388.299
6388.38
6388.689
6388.362
6388.07
6387.805
6387.418
6387.725
6387.559
6387.409
6387.456
6387.287
6387.029
6387.273
6387.071
6386.822
6386.829
6387.765
6388.2
6387.893
6388.523
6388.691
6388.468
6388.569
6388.541
6388.643
6388.661
6388.598
6388.334
6388.309
6388.445
6388.472
6389.171
6389.375
6389.296
6389.54
6389.826
6390.02
6390.342
6390.119
6390.344
6390.477
6390.682
6391.244
6391.464
6391.297
6391.242
6390.829
6390.613
6390.534
6390.283
6390.064
6390.465
6389.962
6390.33
6390.57
6390.16
6390.645
6390.388
6389.975
6390.177
6389.981
6389.698
6389.343
6389.952
6389.991
6389.442
6389.373
6388.999
6388.927
6389.055
6388.958
6389.13
6389.069
6389.139
6389.672
6389.111
6388.906
6388.863
6388.567
6388.286
6388.499
6388.248
6388.037
6387.822
6387.971
6388.996
6388.816
6389.086
6388.881
6388.835
6389.201
6389.133
6388.871
6389.161
6389.104
6388.914
6388.534
6388.771
6388.259
6387.931
6388.242
6387.267
6387.164
6386.629
6386.956
6387.098
6387.53
6387.553
6387.74
6388.154
6388.473
6388.264
6382.794
6383.527
6383.698
6383.597
6383.997
6384.154
6384.166
6384.36
6384.455
6385.582
6386.127
6386.268
6386.25
6386.869
6386.608
6386.669
6386.527
6386.618
6386.365
6386.13
6386.445
6386.701
6386.971
6386.891
6387.162
6386.744
6386.549
6386.712
6386.901
6387.046
6386.881
6386.869
6387.395
6387.547
6387.543
6387.795
6387.607
6387.258
6387.746
6387.398
6387.864
6387.796
6387.26
6387.694
6387.088
6386.971
6387.051
6386.756
6386.21
6386.292
6386.617
6387.085
6387.631
6387.437
6386.995
6387.23
6387.089
6386.923
6386.782
6386.759
6387.24
6387.293
6387.493
6387.548
6387.462
6388.022
6388.063
6388.014
6388.44
6387.949
6387.659
6387.886
6387.327
6387.667
6387.992
6387.994
6387.868
6388.14
6388.13
6387.95
6387.951
6388.006
6387.995
6387.791
6387.908
6388.209
6389.212
6389.237
6389.335
6389.481
6389.83
6390.731
6390.75
6391.188
6390.788
6390.959
6390.711
6390.642
6390.446
6389.622
6388.83
6389.374
6389.368
6388.906
6388.556
6388.432
6388.552
6388.078
6387.863
6388.505
6388.9
6388.442
6388.333
6388.347
6388.436
6388.286
6388.597
6388.729
6388.587
6388.882
6388.877
6389.118
6388.936
6388.383
6388.107
6388.299
6388.38
6388.689
6388.362
6388.07
6387.805
6387.418
6387.725
6387.559
6387.409
6387.456
6387.287
6387.029
6387.273
6387.071
6386.822
6386.829
6387.765
6388.2
6387.893
6388.523
6388.691
6388.468
6388.569
6388.541
6388.643
6388.661
6388.598
6388.334
6388.309
6388.445
6388.472
6389.171
6389.375
6389.296
6389.54
6389.826
6390.02
6390.342
6390.119
6390.344
6390.477
6390.682
6391.244
6391.464
6391.297
6391.242
6390.829
6390.613
6390.534
6390.283
6390.064
6390.465
6389.962
6390.33
6390.57
6390.16
6390.645
6390.388
6389.975
6390.177
6389.981
6389.698
6389.343
6389.952
6389.991
6389.442
6389.373
6388.999
6388.927
6389.055
6388.958
6389.13
6389.069
6389.139
6389.672
6389.111
6388.906
6388.863
6388.567
6388.286
6388.499
6388.248
6388.037
6387.822
6387.971
6388.996
6388.816
6389.086
6388.881
6388.835
6389.201
6389.133
6388.871
6389.161
6389.104
6388.914
6388.534
6388.771
6388.259
6387.931
6388.242
6387.267
6387.164
6386.629
6386.956
6387.098
6387.53
6387.553
6387.74
6388.154
6388.473
6388.264
6411.21
6411.224
6411.487
6411.093
6410.788
6410.318
6410.339
6410.519
6410.252
6410.129
6410.19
6410.805
6410.913
6410.935
6410.8
6410.558
6410.938
6410.42
6410.43
6410.437
6410.259
6410.264
6409.845
6409.711
6409.445
6409.395
6409.164
6409.189
6409.049
6408.855
6409.023
6409.066
6409.496
6408.78
6408.404
6408.289
6408.24
6408.454
6408.641
6409.045
6408.844
6408.918
6409.024
6409.6
6410.199
6410.045
6410.152
6409.718
6409.35
6408.799
6408.313
6407.513
6407.434
6407.48
6407.311
6407.143
6406.862
6407.18
6407.688
6380.397
6380.491
6380.492
6380.22
6380.3
6380.322
6380.321
6380.571
6381.033
6381.22
6380.823
6380.973
6381.228
6380.949
6381.02
6381.07
6381.306
6381.552
6381.664
6381.455
6380.871
6380.925
6380.771
6381.317
6380.832
6380.61
6380.616
6380.765
6380.682
6380.683
6380.576
6380.793
6380.796
6380.704
6380.406
6380.586
6380.345
6380.43
6380.72
6380.572
6380.245
6380.166
6380.507
6380.847
6380.782
6380.337
6379.789
6380.068
6380.14
6379.863
6379.235
6379.398
6379.061
6379.098
6379.068
6379.01
6379.077
6378.602
6378.262
6378.52
6379.09
6379.282
6379.109
6379.382
6379.069
6379.291
6378.99
6379.146
6378.898
6378.933
6379.138
6379.081
6378.67
6378.292
6378.424
6378.372
6378.649
6378.759
6378.585
6378.338
6378.045
6377.573
6377.59
6377.727
6377.622
6377.258
6377.254
6377.33
6377.204
6377.541
6377.476
6377.602
6377.029
6377.244
6377.481
6377.611
6377.993
6378.244
6377.922
6377.748
6377.738
6377.49
6377.429
6377.216

"""

# Split the string by whitespace and convert each to a float
numbers = [float(num) for num in numbers_str.split()]

# Extract last digits
last_digits = [int(str(num)[-1]) for num in numbers]

# Count the frequency of each last digit
digit_counts = Counter(last_digits)

# Find the most common digits
most_common_digits = digit_counts.most_common(9)  # Top 3 most common digits

# Display the results
for i, (digit, count) in enumerate(most_common_digits, start=1):
    print(f"{i} mode: Last digit {digit} appeared {count} times")