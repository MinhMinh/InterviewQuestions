import sys

def isPrime(x):
    if x < 2: return False
    if x == 2 or x == 3: return True
    if x % 6 == 0 or x % 6 == 2 or x % 6 == 3 or x % 6 == 4: return False
    
    y = 3
    while y * y <= x:
        if x % y == 0: return False
        y += 2
        
    return True

test_cases = open(sys.argv[1], 'r').readlines()

for test in test_cases:
    index = test.split(",")
    N = int(index[0])
    M = int(index[1])
    cnt = 0
    for i in range(N, M + 1):
        if isPrime(i):
            cnt += 1
    
    print cnt
    
    

