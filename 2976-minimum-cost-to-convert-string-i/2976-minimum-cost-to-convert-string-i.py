class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        
        adj = defaultdict(list)
        for src, dst, ct in zip(original, changed, cost):
            adj[src].append((dst, ct))

        def dijkstra(src):

            heap = [(0, src)]
            min_cost_map = {}
            
            while heap:
                ct, cur = heapq.heappop(heap)
                
                if cur in min_cost_map:
                    continue
                
                min_cost_map[cur] = ct
                
                for nei, ct2 in adj[cur]:
                    nct = ct + ct2
                    heapq.heappush(heap, (nct, nei))

            return min_cost_map

        min_cost_maps = {c:dijkstra(c) for c in set(source)}
        res = 0
        
        for src, dst in zip(source, target):
            if dst not in min_cost_maps[src]:
                return -1
            
            res += min_cost_maps[src][dst]
        
        return res