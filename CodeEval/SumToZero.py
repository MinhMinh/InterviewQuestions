import sys

test_cases = open(sys.argv[1], 'r').readlines()

for test in test_cases:
    a = map(int, test.strip().split(','))
    n = len(a)
    
    a.sort()
    
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for h in range(k + 1, n):
                    if a[i] + a[j] + a[k] + a[h] == 0:
                        cnt += 1
                  
    print cnt
