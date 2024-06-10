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
    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return None

        queue = [root]

        while queue:
            level = []
            for i in range(len(queue)):
                cur = queue.pop(0)
                if cur:
                    level.append(cur)
                    queue.append(cur.left)
                    queue.append(cur.right)

            if level:
                prev = level[0]
                for cur in level[1:]:
                    if cur:
                        prev.next = cur
                        prev = cur
        
        return root
        
        