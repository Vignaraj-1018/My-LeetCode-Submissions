class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        maxHeap = [-g for g in gifts]
        heapq.heapify(maxHeap)
        for _ in range(k):
            cur = heapq.heappop(maxHeap)
            cur = math.floor((-cur) ** 0.5)
            heapq.heappush(maxHeap, -cur)
            # print(cur, math.floor((-cur) ** 0.5))
            # print(maxHeap)
            
        return -sum(maxHeap)