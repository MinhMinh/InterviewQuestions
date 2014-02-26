import sys

f = open(sys.argv[1], 'r')
test = f.readline()

while test:
    if test[-2] in "13579":
        print 0
    else:
        print 1
    test = f.readline() 
        
f.close()
