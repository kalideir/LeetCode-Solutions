# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution: # Depth First Search based
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        
        if root is None:
            return []
        elif root.right is None and root.left is None:
            return [str(root.val)]
        else:
            paths = self.binaryTreePaths(root.left) + self.binaryTreePaths(root.right)
            return [str(root.val) + '->' + path for path in paths]
                
