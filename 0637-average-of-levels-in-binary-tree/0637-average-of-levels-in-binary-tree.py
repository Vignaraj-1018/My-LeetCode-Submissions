# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = [root]
        
        res = []

        while q:
            
            level = []
            
            for _ in range(len(q)):
                temp = q.pop(0)
                
                if temp:
                    q.append(temp.left)
                    q.append(temp.right)
                    level.append(temp.val)
            
            if level:
                res.append(sum(level)/len(level))
        
        return res