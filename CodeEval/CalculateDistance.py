import sys

f = open(sys.argv[1], 'r')
test = f.readline()

while test:
    points = test.split(' ')
    
    xP1 = int(points[0][1:-1])
    yP1 = int(points[1][:-1])
    
    xP2 = int(points[2][1:-1])
    yP2 = int(points[3][:-2])
    
    d = pow((xP1 - xP2), 2) + pow((yP1 - yP2), 2)
    print "%.0f" % pow(d, 0.5)

    test = f.readline()

f.close()
