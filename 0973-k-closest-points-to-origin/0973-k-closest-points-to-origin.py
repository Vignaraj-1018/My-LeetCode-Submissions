class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k == len(points):
            return points
        heap = []
        res = []
        heapq.heapify(heap)

        for point in points:
            dis = math.sqrt((point[0]**2) + (point[1]**2))
            heapq.heappush(heap, (dis, point))
        
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res