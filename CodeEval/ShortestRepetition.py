import sys

f = open(sys.argv[1], 'r')

test = f.readline()

while test:
    test = test[:-1]
    n = len(test)
    
    r = n
    for i in range(1, n):
        if n % i == 0:
            t = test[0:i] * (n / i)
            if t == test:
                r = i
                break
                    
    print r
    test = f.readline()

f.close()
