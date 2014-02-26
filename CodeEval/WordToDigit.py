import sys

f = open(sys.argv[1], 'r')
test = f.readline()

t = {
    "zero" : "0",
    "one"  : "1",
    "two"  : "2",
    "three": "3",
    "four" : "4",
    "five" : "5",
    "six"  : "6",
    "seven": "7",
    "eight": "8",
    "nine" : "9"
}
while test:
    words = test[:-1].split(';')
    r = ""
    for w in words:
        r = r + t[w.lower()]
    
    print r
    test = f.readline()
    
f.close()
