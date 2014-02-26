import sys

def isInsideCircle(xC, yC, rC, xP, yP):
    return (xC - xP) * (xC - xP) + (yC - yP) * (yC - yP) <= rC * rC

test_cases = open(sys.argv[1], 'r').readlines()

for test in test_cases:
    sp = test.split(' ')
    xCircle = float(sp[1][1:-1])
    yCircle = float(sp[2][:-2])
    rCircle = float(sp[4][:-1])
    xPoint = float(sp[6][1:-1])
    yPoint = float(sp[7][:-2])
    
    r = isInsideCircle(xCircle, yCircle, rCircle, xPoint, yPoint)
    if r: 
        print "true"
    else:
        print "false"
