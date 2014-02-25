class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        cnt = [0] * 3
        for i in A:
            cnt[i] += 1
        
        A = []
        for i in range(3):
            for j in range(cnt[i]):
                A.append(i)
        return A
        
        
r = Solution()
A = [0]

print A
A = r.sortColors(A)
print A
