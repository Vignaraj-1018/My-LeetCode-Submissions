class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        N = len(points)
        adjList = {i:[] for i in range(N)}

        for i in range(N):
            x1,y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adjList[i].append([dist, j])
                adjList[j].append([dist, i])

        res = 0
        visit = set()
        minHeap = [(0,0)]
        heapq.heapify(minHeap)

        while len(visit) < N:
            cost, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            
            res += cost
            visit.add(node)

            for c, n in adjList[node]:
                if n not in visit:
                    heapq.heappush(minHeap, [c, n])

        return res