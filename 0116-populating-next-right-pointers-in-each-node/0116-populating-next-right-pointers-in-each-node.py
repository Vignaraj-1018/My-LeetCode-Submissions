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
            for i in range(len(q)):
                cur = q.pop(0)
                if cur:
                    level.append(cur)
                    q.append(cur.left)
                    q.append(cur.right)
            
            if level:
                prev = level[0]
                
                for cur in level[1:]:
                    if cur:
                        prev.next = cur
                        prev = cur
            
        return root