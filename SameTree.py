# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
"""
This problem  better understood when imagining the trees at smaller sizes, say single node, or 1-level trees then build up
"""
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q: # both parent nodes have same side children as none => equal
            return True
        if not q or not p: # one or both parents have diff children
            return False
        if p.val != q.val: 
            return False
        """
        till here we checked if current current nodes are not equaling each other [base cases of recursion],
        next we define the recursion for left and right nodes for the next nodes (children)
        """
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
