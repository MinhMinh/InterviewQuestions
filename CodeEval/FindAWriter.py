import sys

f = open(sys.argv[1], 'r')
test = f.readline()

while test:
    sp = test.strip().split('|')
    code = map(int, sp[1].strip().split(' '))
    name = ""
    for i in code:
        name = name + sp[0][i - 1]
    print name
    
    test = f.readline()
    
f.close()
