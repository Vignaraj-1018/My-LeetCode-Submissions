# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = [root]
        res = []
        flag = False
        while q:
            
            cur = []
            for i in range(len(q)):
                temp = q.pop(0)
                if temp:
                    q.append(temp.left)
                    q.append(temp.right)
                    cur.append(temp.val)
            if cur and flag:
                cur = cur[::-1]
            if cur:
                res.append(cur)
                flag = not flag

        
        return res
        