import sys

test_cases = open(sys.argv[1], 'r').readlines()

for test in test_cases:
    N = int(test)
    sum = 0
    sum += N / 5
    N %= 5
    sum += N / 3
    N %= 3
    sum += N

    print sum
