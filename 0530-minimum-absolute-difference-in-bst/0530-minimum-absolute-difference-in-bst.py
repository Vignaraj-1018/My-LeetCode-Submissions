# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        min_diff, prev = [float("inf")], [None]
        
        def in_order_traversal(node):
            if node is None:
                return
            in_order_traversal(node.left)
            
            if prev[0] is not None:
                min_diff[0] = min(min_diff[0], node.val - prev[0])
            prev[0] = node.val
            in_order_traversal(node.right)
        
        in_order_traversal(root)
        return min_diff[0]