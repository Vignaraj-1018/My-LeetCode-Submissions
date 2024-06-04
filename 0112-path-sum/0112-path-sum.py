# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        pathSum = [0]
        
        def dfs(node):
            
            if not node:
                return False
            
            pathSum[0] += node.val
            
            if not node.left and not node.right and pathSum[0] == targetSum:
                return True
            
            has_left = dfs(node.left) if node.left else False
            has_right = dfs(node.right) if node.right else False
            
            pathSum[0] -= node.val
            
            return has_left or has_right
        
        
        return dfs(root)