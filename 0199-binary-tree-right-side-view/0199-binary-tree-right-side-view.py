# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = []
        queue.append(root)
        while queue:
            level = []
            for i in range(len(queue)):
                cur = queue.pop(0)
                if cur:
                    queue.append(cur.left)
                    queue.append(cur.right)
                    level.append(cur.val)
            if level:
                res.append(level[-1])

        return res