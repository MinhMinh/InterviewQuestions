class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        d = [[0] * n for i in range(m)]
        
        d[0][0] = grid[0][0]
        for i in range(1, m):
            d[i][0] = d[i - 1][0] + grid[i][0]
        for j in range(1, n):
            d[0][j] = d[0][j - 1] + grid[0][j]
            
        for i in range(1, m):
            for j in range(1, n):
                d[i][j] = min(d[i - 1][j], d[i][j - 1]) + grid[i][j]
        
        return d[m - 1][n - 1]
