import sys

f = open(sys.argv[1], 'r')
test = f.readline()

while test:
    a = map(int, test.strip().split(' '))
    
    cnt = [0] * 10
    for i in a:
        cnt[i] += 1
    
    r = 0
    for i in range(1, 10):
        if cnt[i] == 1:
            r = i
            break    
    
    for i in range(len(a)):
        if a[i] == r:
            r = i + 1
            break
            
    print r
    
    test = f.readline()
