class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        maxHeap = [-g for g in gifts]
        heapq.heapify(maxHeap)
        
        for _ in range(k):
            heapq.heappush(maxHeap, -floor((-heapq.heappop(maxHeap)) ** 0.5))
            
        return -sum(maxHeap)