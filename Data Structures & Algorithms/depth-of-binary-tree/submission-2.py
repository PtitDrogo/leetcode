# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        if root == None:
            return 0
        return self.advance(root, 1)

    def advance(self, root: Optional[TreeNode], level) -> int:
        if root.left == None and root.right == None:
            return level
        level1 = level2 = level
        if root.left:
            level1 = self.advance(root.left, level)
        if root.right:
            level2 = self.advance(root.right, level)
        return max(level1, level2) + 1
            
