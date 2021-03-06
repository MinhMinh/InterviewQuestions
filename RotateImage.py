class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        n = len(matrix)  #3 --> 1, 2 --> 0
        for i in range((n + 1) / 2):
            for j in range(n / 2):
                #i, j --> j, n - i - 1 --> n - i - 1, n - j - 1 --> n - j - 1, i --> i, j
                print i, j
                t = matrix[i][j]
                matrix[i][j] = matrix[n - j - 1][i]
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
                matrix[j][n - i - 1] = t
                
        return matrix
        
    def rotate_extra(self, matrix):
        n = len(matrix)
        m = [[-1] * n for i in range(n)]
        u, v = 0, 0
        for j in range(n):
            for i in range(n - 1, -1, -1):
                m[u][v] = matrix[i][j]
                v += 1
                if v == n:
                    v = 0
                    u += 1
        return m 
        
        
run = Solution()
matrix = run.rotate_extra([[1, 2, 3, 4],[5, 6, 7,8],[9, 10, 11, 12],[13, 14, 15, 16]])

for i in range(len(matrix)):
    for j in range(len(matrix)):
        print '{:2}'.format(matrix[i][j]),
    print 
