class Solution:
    def dfs(self, node: int, vis: List[int], adj: List[List[int]], temp: List[int]):
        vis[node] = 1
        temp[node] = 1

        for neighbor in adj[node]:
            if vis[neighbor] == 0:
                self.dfs(neighbor, vis, adj, temp)
    
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        adj1 = [[] for _ in range(n)]

        for edge in invocations:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

            adj1[edge[0]].append(edge[1])

        vis = [0] * n
        temp = [0] * n
        vis1 = [0] * n
        temp1 = [0] * n

        self.dfs(k, vis, adj, temp)
        self.dfs(k, vis1, adj1, temp1)

        ans = []

        if temp == temp1:
            for i in range(n):
                if temp[i] == 0:
                    ans.append(i)
        else:
            for i in range(n):
                ans.append(i)

        return ans