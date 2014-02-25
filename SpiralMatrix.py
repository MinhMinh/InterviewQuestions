class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        m = len(matrix)
        if m == 0: return []
        n = len(matrix[0])
        
        r = []
        for k in range(0, min((m - 1) / 2, (n - 1) / 2) + 1):
            for j in range(k, n - k):
                r.append(matrix[k][j])
            for i in range(k + 1, m - k):  
                r.append(matrix[i][n - k - 1])
            if m - k - 1 != k:
                for j in range(n - k - 2, k - 1, -1):
                    r.append(matrix[m - k - 1][j])
            if k != n - k - 1:
                for i in range(m - k - 2, k, -1):
                    r.append(matrix[i][k])
        
        return r
        
      
r = Solution()
matrix = [
 [ 1,  2,  3 ],
 [ 4,  5,  6 ],
 [ 7,  8,  9 ],
 [10, 11, 12 ]
]

matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]]
          
matrix = [[1, 2, 3, 4]]

matrix = [[1], [2], [3], [4]]
print r.spiralOrder(matrix);
