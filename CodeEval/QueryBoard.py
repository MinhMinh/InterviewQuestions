import sys

f = open(sys.argv[1], 'r')
line = f.readline().strip()

board = [[0] * 256 for i in range(256)]

while line:
    sp = line.split(' ')
    
    if sp[0] == "SetRow":
        row = int(sp[1])
        for i in range(256):
            board[row][i] = int(sp[2])
    elif sp[0] == "SetCol":
        col = int(sp[1])
        for i in range(256):
            board[i][col] = int(sp[2])
    elif sp[0] == "QueryRow":
        row = int(sp[1])
        sum = 0
        for i in range(256):
            sum += board[row][i]
        print sum
    else: #QueryCol
        col = int(sp[1])
        sum = 0
        for i in range(256):
            sum += board[i][col]
        print sum
        
    line = f.readline().strip()
