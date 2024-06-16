# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        res = [0]
        
        def dfs(root, path):
            
            if not root:
                return
            
            path = path*10 + int(root.val)
            
            if not root.left and not root.right:
                res[0] += path
            else:
                dfs(root.left, path)
                dfs(root.right, path)
        
            path //= 10
        
        dfs(root, 0)
        
        return res[0]