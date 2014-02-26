import sys

f = open(sys.argv[1], 'r')

d = [
    ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
    ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
    ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
    ["M", "MM", "MMM"]
    ]
test = f.readline()

while test:
    n = int(test)
    r = ""
    if n % 10 != 0:
        r = d[0][n % 10 - 1] + r
    n /= 10
    if n % 10 != 0:
        r = d[1][n % 10 - 1] + r
    n /= 10
    if n % 10 != 0:
        r = d[2][n % 10 - 1] + r
    n /= 10
    if n % 10 != 0:
        r = d[3][n % 10 - 1] + r                
    
    print r
    test = f.readline()

f.close()
