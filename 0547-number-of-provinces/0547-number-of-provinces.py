class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def dfs(node):
            
            visited[node] = 1
            
            for i in adjList[node]:
                if not visited[i]:
                    dfs(i)
            
        n = len(isConnected)
        visited = [0] * (n + 1)
        
        adjList = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] and i != j:
                    adjList[i].append(j)
                    adjList[j].append(i)

        # print(adjList, visited)
        
        # return 1
        cnt = 0
        for i in range(n):
            if not visited[i]:
                cnt+=1
                dfs(i)
        
        return cnt
        