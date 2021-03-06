import sys

f = open(sys.argv[1], 'r')

def find(n):
    if n == 0: return 0
    
    k = 0
    while pow(2, k) <= n:
        k += 1
    k -= 1
    
    return (find(n - pow(2, k)) + 1) % 3       

test = f.readline()
while test:
    n = int(test)
    
    print find(n)
    test = f.readline()
    
f.close()
