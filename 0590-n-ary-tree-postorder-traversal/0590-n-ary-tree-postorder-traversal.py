"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        
        if not root:
            return res
        
        stack = [(root,False)]
        
        while stack:
            node, visited = stack.pop()
            
            if visited:
                res.append(node.val)
            else:
                stack.append((node, True))
                for c in node.children[::-1]:
                    stack.append((c, False))
        return res
        
#         def dfs(node):
#             if not node:
#                 return
            
#             for child in node.children:
#                 dfs(child)
            
#             res.append(node.val)
        
#         dfs(root)
#         return res