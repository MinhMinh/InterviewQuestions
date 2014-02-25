# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        self.longest = 0
        self.travel(root, 1)
        return self.longest
        
    def travel(self, node, level):
        if node is None:
            self.longest = max(self.longest, level - 1)
            return
        self.travel(node.left, level + 1)
        self.travel(node.right, level + 1)
        
      
r = Solution()
root = TreeNode(12)
print r.maxDepth(root)
