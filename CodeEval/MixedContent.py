import sys

f = open(sys.argv[1], 'r')

test = f.readline()
while test:
    ws = test[:-1].split(",")
    words = ""
    digits = ""
    for w in ws:
        if w.isdigit():
            digits += w + ","
        else:
            words += w + ","

    r = ""
    if words != "":
        r = words[:-1]
    if words != "" and digits != "":
        r += "|"
    if digits != "":
        r += digits[:-1]
        
    print r    
    test = f.readline()

f.close()
