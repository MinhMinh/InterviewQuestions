import sys

f = open(sys.argv[1], 'r')

test = f.readline()
while test:
    ps = test[:-1].split(", ")
    
    x = []
    y = []
    for p in ps:
        sp = p.split(",")
        x.append(int(sp[0][1:]))
        y.append(int(sp[1][:-1]))    

    d = []
    for i in range(3):
        d.append(pow(x[i] - x[(i + 1) % 3], 2) + pow(y[i] - y[(i + 1) % 3], 2))  

    d.sort()
    if d[0] + d[1] != d[2] or d[0] != d[1] or d[0] == 0: 
        print "false"
    else:
        e = []
        for i in range(3):
            e.append(pow(x[i] - x[3], 2) + pow(y[i] - y[3], 2))  
        e.sort()
        if e[0] + e[1] != e[2] or e[0] != e[1] or e[0] == 0:
            print "false"
        elif e[0] != d[0] or e[2] != d[2]:
            print "false"
        else:
            print "true"
        
    test = f.readline()
    
f.close()
