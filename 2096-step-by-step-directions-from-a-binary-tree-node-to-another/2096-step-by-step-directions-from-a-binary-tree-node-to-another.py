# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def dfs(node, path, target):
            if not node:
                return []
            
            if node.val == target:
                return path
            
            path.append('L')
            if dfs(node.left, path, target):
                return path
            path.pop()

            path.append('R')
            if dfs(node.right, path, target):
                return path
            path.pop()

            return []
        
        start = dfs(root, [], startValue)
        dest = dfs(root, [], destValue)

        i = 0
        l = min(len(start) , len(dest))
        while i < l and start[i] == dest[i]:
            i += 1
        
        res = ["U"] * len(start[i:]) + dest[i:]
            
        return "".join(res)
            