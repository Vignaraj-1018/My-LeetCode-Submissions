class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        maxHeap = [-g for g in gifts]
        heapq.heapify(maxHeap)
        
        for _ in range(k):
            heapq.heappush(maxHeap, -floor(sqrt(-heapq.heappop(maxHeap))))
            
        return -sum(maxHeap)