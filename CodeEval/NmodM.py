import sys

test_cases = open(sys.argv[1], 'r').readlines()

for test in test_cases:
    N, M = test.split(",")
    N = int(N)
    M = int(M)
    
    d = N / M
    r = N - d * M
    
    print r
