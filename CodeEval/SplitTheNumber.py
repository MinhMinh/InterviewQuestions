import sys

f = open(sys.argv[1], 'r')
test = f.readline()

while test:
    sp = test[:-1].split(' ')
    index = sp[1].find('-')
    if index == -1:
        index = sp[1].find('+')
        
    a = int(sp[0][0:index])
    b = int(sp[0][index:])

    if '-' in sp[1]:    
        print a - b
    else:
        print a + b
    
    test = f.readline()
    
f.close()
