import sys

f = open(sys.argv[1], 'r')
line = f.readline()

while line:
    sp = line.strip().split('|')
    a = map(int, sp[0].strip().split(' '))
    b = map(int, sp[1].strip().split(' '))
    
    print ' '.join(map(str, [x * y for x, y in zip(a, b)]))
    
    line = f.readline()
