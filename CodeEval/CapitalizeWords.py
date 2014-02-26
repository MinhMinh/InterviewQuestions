import sys

f = open(sys.argv[1], 'r')
test = f.readline()

while test:
    test = test.strip()
    test = " " + test
    r = ""
    i = 0
    while i < len(test):
        if test[i] == ' ' and test[i + 1].isalpha():
            r = r + test[i] + test[i + 1].upper()
            i += 2
        else:
            r = r + test[i]
            i += 1

    print r[1:]
    test = f.readline()
    
f.close()
