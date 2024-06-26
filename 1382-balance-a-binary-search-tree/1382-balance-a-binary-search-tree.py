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
        
        def createBst(inOrder,l,h):
            if (l>h):
                return None
            
            m = (l + h) // 2
            
            root = TreeNode(inOrder[m])
            root.left = createBst(inOrder,l,m-1)
            root.right = createBst(inOrder,m+1,h)
            return root

        return createBst(inOrder, 0, len(inOrder)-1)