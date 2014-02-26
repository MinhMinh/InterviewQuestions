import sys

f = open(sys.argv[1], 'r')
test = f.readline()

while test:
    a = map(int, test[:-1].split(','))
    
    L = len(a)
    r = "None"
    
    count = [0] * 101
    for i in a:
        count[i] += 1
        if count[i] * 2 > L:
            r = i
            break
    
    print r
    
    test = f.readline()
    
f.close()
