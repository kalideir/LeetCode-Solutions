# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    
    def height(self, node):
        if not node: return 0 # base case for the recursive function
        else:
            return max(self.height(node.left), self.height(node.right)) + 1 # e.g., when sindle child => 0 + 1, 0 from base
        
    
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True # when no child => balanced by default
        else:
            return abs(self.height(root.left) - self.height(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
