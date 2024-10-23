# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level_sum = []
        
        queue = [root]
        while queue:
            cur = 0
            for _ in range(len(queue)):
                node = queue.pop(0)
                cur += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level_sum.append(cur)
            
        
        queue = [(root, root.val)]
        level = 0
        while queue:
            for _ in range(len(queue)):
                
                node, val = queue.pop(0)
                node.val = level_sum[level] - val
                
                child_sum = 0
                if node.left:
                    child_sum += node.left.val
                if node.right:
                    child_sum += node.right.val
                    
                if node.left:
                    queue.append((node.left, child_sum))
                if node.right:
                    queue.append((node.right, child_sum))
                    
            level += 1
            
        return root