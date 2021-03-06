class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        self.sum = 0
        self.travel(root, 0)
        return self.sum
        
    def travel(self, node, value):
        if node is None:
            return
        
        if node.right is None and node.left is None:
            self.sum += value * 10 + node.val
            
        self.travel(node.right, value * 10 + node.val)
        self.travel(node.left, value * 10 + node.val)
        
        
r = Solution()

root = TreeNode(9)
root.right = TreeNode(1)

print r.sumNumbers(root)
