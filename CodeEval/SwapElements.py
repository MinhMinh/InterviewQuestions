import sys

f = open(sys.argv[1], 'r')
test = f.readline()

while test:
    sp = test.strip().split(':')
    a = sp[0].strip().split(' ')
    sp[1] = sp[1].strip() + ","
    b = sp[1].split(' ')

    for c in b:
        x, y = map(int, c[:-1].split('-'))
        t = a[x]
        a[x] = a[y]
        a[y] = t
        
    print ' '.join(a)    
    
    test = f.readline()
    
f.close()
