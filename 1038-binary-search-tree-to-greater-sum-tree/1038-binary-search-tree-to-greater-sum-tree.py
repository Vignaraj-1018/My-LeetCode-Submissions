# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        _sum = 0
        
        def dfs(root):
            if not root:
                return
            
            nonlocal _sum
            dfs(root.right)
            temp = root.val
            root.val += _sum
            _sum += temp
            
            dfs(root.left)
        
        dfs(root)
        return root