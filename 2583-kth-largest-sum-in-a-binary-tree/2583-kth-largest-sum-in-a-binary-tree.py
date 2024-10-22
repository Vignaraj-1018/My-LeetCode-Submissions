# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        min_heap = []
        
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
                
            heapq.heappush(min_heap, cur)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
                
            
        return -1 if len(min_heap) <k else min_heap[0]
                    