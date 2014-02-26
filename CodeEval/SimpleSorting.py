import sys

f = open(sys.argv[1], 'r')
test = f.readline().strip()

while test:
    a = map(float, test.split(' '))
    a.sort()
    
    r = ""
    for i in a:
        r = r + "%.3f " % i        
    
    print r
    test = f.readline().strip()
