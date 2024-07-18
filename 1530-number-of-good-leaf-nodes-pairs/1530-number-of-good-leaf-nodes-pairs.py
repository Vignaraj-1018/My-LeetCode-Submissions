# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
       
        pairs = 0
       
        def dfs(node):
            nonlocal pairs
            if not node:
                return []

            if not node.left and not node.right:
                return [1]
            
            left_dist = dfs(node.left)
            right_dist = dfs(node.right)
         
            for d1 in left_dist:
                for d2 in right_dist:
                    if d1 + d2 <= distance:
                        pairs += 1

            res = left_dist + right_dist
            return [d + 1 for d in res]

        dfs(root)
        return pairs