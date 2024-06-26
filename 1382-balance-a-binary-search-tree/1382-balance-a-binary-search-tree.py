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
        
        def createBst(inOrder):
            if not inOrder:
                return None
            
            m = len(inOrder)//2
            
            root = TreeNode(inOrder[m])
            root.left = createBst(inOrder[:m])
            root.right = createBst(inOrder[m+1:])
            return root

        return createBst(inOrder)