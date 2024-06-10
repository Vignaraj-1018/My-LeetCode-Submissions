"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root:
            return root
        
        q = [root]
        
        while q:
            
            level = []
            n = len(q)
            for i in range(n):
                cur = q.pop(0)
                if cur:
                    level.append(cur)
                    q.append(cur.left)
                    q.append(cur.right)
                    if i < n-1:
                        cur.next = q[0]
            
            
        return root