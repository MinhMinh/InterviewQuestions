import sys

f = open(sys.argv[1], 'r')
test = f.readline()

while test:
    test = " " + test
    index = len(test) - 1
    while test[index] != ' ':
        index -= 1
    end = index
    index -= 1
    while test[index] != ' ':
        index -=1
           
    print test[index + 1:end]
    
    test = f.readline()
    
f.close()
