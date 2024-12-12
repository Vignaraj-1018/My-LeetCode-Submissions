class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        maxHeap = [-g for g in gifts]
        heapq.heapify(maxHeap)
        
        for _ in range(k):
            cur = -heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, -floor(sqrt(cur)))
            
        return -sum(maxHeap)