import sys

f = open(sys.argv[1], 'r')
test = f.readline()

while test:
    words = test[:-1].split(' ')
    best = 0
    for w in words:
        if len(w) > best:
            best = len(w)
            r = w
    
    print r
    
    test = f.readline()
    
f.close()
