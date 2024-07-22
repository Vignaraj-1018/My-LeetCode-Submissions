class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        min_heap = []
        heapq.heapify(min_heap)
        for n, h in zip(names, heights):
            heapq.heappush(min_heap, [h*-1, n])
        res = []
        while min_heap:
            res.append(heapq.heappop(min_heap)[1])
        # print(min_heap)
        
        return res