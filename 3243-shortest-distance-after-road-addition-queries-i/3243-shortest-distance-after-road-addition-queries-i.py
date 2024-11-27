class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj = {i:[i + 1] for i in range(n-1)}
        res = []

        def bfs():
            queue = [(0, 0)]
            visit = set()

            while queue:
                node, dist = queue.pop(0)
                if node == n - 1:
                    return dist
                
                if node in visit:
                    continue

                visit.add(node)
                
                for nei in adj[node]:
                    if nei not in visit:
                        queue.append((nei, dist + 1))
            
        for s, d in queries:
            adj[s].append(d)
            res.append(bfs())
        
        return res