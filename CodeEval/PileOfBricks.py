import sys

def canPass(hole, x1, y1, x2, y2):
    b = [abs(x1 - x2), abs(y1 - y2)]
    b.sort()
    return b[0] <= hole[0] and b[1] <= hole[1]    
    
f = open(sys.argv[1], 'r')

test = f.readline()
while test:
    r = test[:-1].split("|")
    
    p1, p2 = r[0].split(" ")
    x1, y1 = map(int, p1[1:-1].split(","))
    x2, y2 = map(int, p2[1:-1].split(","))
    
    hole = [abs(x1 - x2), abs(y1 - y2)]
    hole.sort()
    
    ans = []
    bricks = r[1].split(";")
    for brick in bricks:
        index, point1, point2 = brick[1:-1].split(" ")
        
        x1, y1, z1 = map(int, point1[1:-1].split(","))
        x2, y2, z2 = map(int, point2[1:-1].split(","))
        
        if canPass(hole, x1, y1, x2, y2):
            ans.append(index)
            continue
        if canPass(hole, z1, y1, z2, y2):
            ans.append(index)
            continue
        if canPass(hole, x1, z1, x2, z2):
            ans.append(index)
            continue        
        
    if len(ans) == 0:
        print "-"
    else:
        print ','.join(ans)
    test = f.readline()
    
f.close()
