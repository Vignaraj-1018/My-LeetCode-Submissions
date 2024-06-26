# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        inOrder = []
        
        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            inOrder.append(root.val)
            dfs(root.right)
            
        
        dfs(root)
        
        def createBST(inOrder, l, h):
            if l > h:
                return None
            
            m = (l + h) // 2
            
            node = TreeNode(inOrder[m])
            node.left = createBST(inOrder, l, m - 1)
            node.right = createBST(inOrder, m + 1, h)
            
            return node
        
        
        return createBST(inOrder, 0, len(inOrder)-1)