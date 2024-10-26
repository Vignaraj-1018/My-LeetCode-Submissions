# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findHeight(self, curr: Optional[TreeNode], level: int, node_level: dict, top2_nodes_at_level: dict) -> int:
        if not curr:
            return 0

        height = 1 + max(self.findHeight(curr.left, level + 1, node_level, top2_nodes_at_level),
                         self.findHeight(curr.right, level + 1, node_level, top2_nodes_at_level))

        node_level[curr.val] = (level, height)

        if height > top2_nodes_at_level[level][0]:
            top2_nodes_at_level[level] = (height, top2_nodes_at_level[level][0])
        elif height > top2_nodes_at_level[level][1]:
            top2_nodes_at_level[level] = (top2_nodes_at_level[level][0], height)

        return height

    def treeQueries(self, root: TreeNode, queries: List[int]) -> List[int]:
        top2_nodes_at_level = defaultdict(lambda: (0, 0))
        node_level = {}

        self.findHeight(root, 0, node_level, top2_nodes_at_level)

        res = []
        for query_node in queries:
            level, height = node_level[query_node]
            max_height = top2_nodes_at_level[level][1] if top2_nodes_at_level[level][0] == height else top2_nodes_at_level[level][0]
            res.append(max_height + level - 1)
        return res
        