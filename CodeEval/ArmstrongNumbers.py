import sys
import math

f = open(sys.argv[1], 'r')
test = f.readline()

while test:
    test = test.strip()
    n = len(test)
    m = int(test.strip())
    s = 0
    for i in test:
        s += math.pow(int(i), n)
    
    print s == m
  
    test = f.readline()
