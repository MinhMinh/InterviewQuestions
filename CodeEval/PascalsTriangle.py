import sys

test_cases = open(sys.argv[1], 'r').readlines()

for test in test_cases:
    print 1, 
    a = [1]
    for i in range(int(test) - 1):
        print 1, 
        b = [1]
        for j in range(len(a) - 1):
            c = a[j] + a[j + 1]
            b.append(c)
            print c, 
            
        b.append(1)
        
        print 1,
        
        a = b
    
    print
