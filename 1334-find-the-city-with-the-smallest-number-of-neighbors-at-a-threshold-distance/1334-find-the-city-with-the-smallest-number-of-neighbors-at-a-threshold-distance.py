class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = defaultdict(list)
        for v1, v2, dist in edges:
            adj[v1].append((v2, dist))
            adj[v2].append((v1, dist))
            
        def dijkstra(src):
            heap = [(0, src)]
            # heapq.heapify(heap)
            visit = set()
            
            while heap:
                
                dist, cur = heapq.heappop(heap)
                if cur in visit:
                    continue
                
                visit.add(cur)
                for nei, d2 in adj[cur]:
                    n_dist = dist + d2
                    if n_dist <= distanceThreshold:
                        heapq.heappush(heap, (n_dist, nei))
            
            return len(visit) - 1
        
        res, min_count = -1, n
        for src in range(n):
            count = dijkstra(src)
            if count <= min_count:
                res, min_count = src, count
            
        
        return res