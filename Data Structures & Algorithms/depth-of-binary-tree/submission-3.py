# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, node: Optional[TreeNode], currlvl: int) -> int:
        if node == None:
            return currlvl
        currlvl += 1
        l = self.helper(node.left, currlvl) 
        r = self.helper(node.right, currlvl)       
        return max(l, r)
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.helper(root, 0)







    