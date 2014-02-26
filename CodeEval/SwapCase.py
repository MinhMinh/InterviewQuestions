import sys

f = open(sys.argv[1], 'r')
test = f.readline()

while test:
    r = ""
    for i in test:
        if i.isalpha():
            if i.islower():
                r = r + chr(ord(i) - 32)
            else:
                r = r + chr(ord(i) + 32)
        else:
            r = r + i    
            
    print r,
    test = f.readline()
    
f.close()
