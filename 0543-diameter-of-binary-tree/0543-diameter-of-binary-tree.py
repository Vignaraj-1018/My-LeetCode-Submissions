# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def depthOfSubTree(root):
            if not root:
                return -1
            
            left = depthOfSubTree(root.left)
            right = depthOfSubTree(root.right)
            res[0] = max(res[0], 2 + left + right)
            return 1 + max(left,right)

        depthOfSubTree(root)
        return res[0]