import sys

f = open(sys.argv[1], 'r')
line = f.readline()

while line:
    (first, second) = line[:-1].split(',')
    first = first + first
    print second in first
    
    line = f.readline()

f.close()
