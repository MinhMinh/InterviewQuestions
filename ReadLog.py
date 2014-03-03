import sys

f = open(sys.argv[1], 'r')

line = f.readline()

r = {}

while line:
    w = line[:-1].split(" ")
    if w[3] == "drops":
        if w[2] in r:
            r[w[2]] += int(w[4])
        else:
            r[w[2]] = int(w[4])

    line = f.readline()

for k in sorted(r):
    print "%s drops total %d packets" % (k, r[k])

f.close()
