import sys

f = open(sys.argv[1], 'r')
test = f.readline()

while test:
    r = ""
    for i in test:
        if 'a' <= i and i <= 'j':
            r = r + chr(ord(i) - ord('a') + ord('0'))   
        if i.isdigit():
            r = r + i
            
    if len(r) == 0:
        r = "NONE" 
    print r
    
    test = f.readline()
    
f.close()
