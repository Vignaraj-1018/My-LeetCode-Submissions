# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balance = [True]
        
        def isSubTreeBalanced(root):
            if not root:
                return 0
            
            left = isSubTreeBalanced(root.left)
            right = isSubTreeBalanced(root.right)
            
            if abs(left-right)>1:
                balance[0] = False
            
            return 1 + max(left,right)
        
        isSubTreeBalanced(root)
        
        return balance[0]
            