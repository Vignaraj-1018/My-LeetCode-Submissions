class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        minHeap = [(n, i) for i, n in enumerate(nums)]
        heapq.heapify(minHeap)
        
        for _ in range(k):
            n, i = heapq.heappop(minHeap)
            n *= multiplier
            heapq.heappush(minHeap,(n, i))
        
        res = [0] * len(nums)
        while minHeap:
            n, i = heapq.heappop(minHeap)
            res[i] = n
        
        return res