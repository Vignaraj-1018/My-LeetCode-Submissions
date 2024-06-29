class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        res = [[] for _ in range(n)]
        directChild = [[] for _ in range(n)]

        def dfs(pat, cur):
            for node in directChild[cur]:
                if not res[node] or res[node][-1] != pat:
                    res[node].append(pat)
                    dfs(pat, node)

        for n1,n2 in edges:
            directChild[n1].append(n2)

        for i in range(n):
            dfs(i, i)
        
        return res
        
            