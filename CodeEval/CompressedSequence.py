import sys

f = open(sys.argv[1], 'r')

test = f.readline()

while test:
    a = test[:-1].split(' ')
    
    r = []
    n = len(a)
    a.append("zzz")
    
    i = 0
    while i < n:
        j = i
        while j < n and a[j] == a[i]:
            j += 1

        r.append(str(j - i))
        r.append(a[i])
        i = j
             
    print ' '.join(r)            
    test = f.readline()

f.close()
