class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        n = len(A)
        for i in range(n - 1):
            if A[i] == 0:
                canPassZero = False
                for j in range(i):
                    if A[j] + j > i:
                        canPassZero = True
                        break
                if canPassZero == False: return False
        return True
        
r = Solution()
print r.canJump([2,3,1,1,4])
print r.canJump([3,2,1,0,4])
