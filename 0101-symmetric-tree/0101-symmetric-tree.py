# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def isSysmmetric(level):
            i, j = 0, len(level)-1
            
            while i<j:
                if level[i]!=level[j]:
                    return False
                i+=1
                j-=1
            return True
            
        q = [root]
        
        while q:
            level = []
            for _ in range(len(q)):
                cur = q.pop(0)
                if not cur:
                    level.append(None)
                if cur:
                    level.append(cur.val)
                    q.append(cur.left)
                    q.append(cur.right)
            if not isSysmmetric(level):
                return False
        
        return True