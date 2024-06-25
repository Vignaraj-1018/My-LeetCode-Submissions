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
            tmp = root.val
            root.val += _sum
            _sum += tmp
            dfs(root.left)

        
        dfs(root)
        return root
