import sys

lines = open(sys.argv[1], 'r').readlines()

d = [0]
for line in lines:
    numbers = map(int, line.strip().split(' '))
    
    n = len(numbers)
    t = [0] * n
    t[0] = d[0] + numbers[0]
    for i in range(1, n - 1):
        t[i] = max(d[i - 1], d[i]) + numbers[i]
    t[n - 1] = d[n - 2] + numbers[n - 1]
    d = t
    
print max(d)
