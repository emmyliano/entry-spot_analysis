import statistics
from collections import Counter

# Vertically formatted string of numbers
numbers_str = """
6480.494
6480.866
6481.269
6481.259
6481.324
6481.479
6481.419
6481.805
6482.007
6481.755
6481.197
6481.007
6481.866
6481.753
6481.553
6482.073
6482.042
6482.009
6481.899
6482.112
6482.594
6482.399
6482.555
6482.717
6482.451
6483.307
6483.756
6483.631
6483.704
6483.072
6482.512
6482.632
6482.497
6482.002
6481.885
6481.557
6481.727
6482.036
6481.279
6481.284
6481.758
6481.601
6481.634
6481.741
6481.73
6481.653
6482.348
6482.487
6482.976
6483.098
6482.915
6483.261
6482.846
6482.992
6482.685
6482.511
6482.229
6482.274
6482.54
6483.021
6482.707
6483.256
6483.412
6483.903
6484.291
6483.973
6483.788
6484.011
"""

# Split the string by whitespace and convert each to a float
numbers = [float(num) for num in numbers_str.split()]

# Extract last digits
last_digits = [int(str(num)[-1]) for num in numbers]

# Count the frequency of each last digit
digit_counts = Counter(last_digits)

# Find the most common digits
most_common_digits = digit_counts.most_common(3)  # Top 3 most common digits

# Display the results
for i, (digit, count) in enumerate(most_common_digits, start=1):
    print(f"{i} mode: Last digit {digit} appeared {count} times")