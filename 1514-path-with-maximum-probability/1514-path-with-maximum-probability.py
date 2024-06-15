class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = {i:[] for i in range(n)}

        for i, (v, u) in enumerate(edges):
            adj[v].append((u, succProb[i]))
            adj[u].append((v, succProb[i]))

        distances = [0] * n
        distances[start_node] = 1

        pq = [[-1, start_node]]

        heapq.heapify(pq)

        while pq:

            cur_dist, cur_node = heapq.heappop(pq)
            cur_dist = -cur_dist
            
            if cur_node == end_node:
                return cur_dist

            if cur_dist < distances[cur_node]:
                continue

            for nei, nei_dist in adj[cur_node]:
                dist = cur_dist * nei_dist
                if dist > distances[nei]:
                    distances[nei] = dist
                    heapq.heappush(pq, [-dist, nei])
        
        return distances[end_node]
