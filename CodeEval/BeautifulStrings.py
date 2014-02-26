import sys

test_cases = open(sys.argv[1], 'r').readlines()

for test in test_cases:
    test = test.lower()
    f = [0] * 26
    for i in test:
        if i.isalpha():
            f[ord(i) - ord('a')] += 1
    f.sort()
    sum = 0
    for i in range(26):
        sum += f[i] * (i + 1)       
    print sum
    
