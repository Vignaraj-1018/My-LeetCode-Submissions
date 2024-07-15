# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        node_map = {}
        children = set()

        for item in descriptions:
            if item[0] not in node_map:
                node_map[item[0]] = TreeNode(item[0])
            if item[1] not in node_map:
                node_map[item[1]] = TreeNode(item[1])
            if item[2]:
                node_map[item[0]].left = node_map[item[1]]
            else:
                node_map[item[0]].right = node_map[item[1]]
            children.add(item[1])

        for i in descriptions:
            if i[0] not in children:
                return node_map[i[0]]