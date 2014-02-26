import sys

f = open(sys.argv[1], 'r')

test = f.readline()

while test:
    cities = test.strip().split(';')
    d = []
    for city in cities:
        sp = city.strip().split(',')
        if len(sp) == 2:
            d.append(int(sp[1]))
        
    d.sort()
    
    for i in range(len(d) - 1, 0, -1):
        d[i] = d[i] - d[i - 1]
    
    print ','.join(map(str, d))
    
    test = f.readline()
