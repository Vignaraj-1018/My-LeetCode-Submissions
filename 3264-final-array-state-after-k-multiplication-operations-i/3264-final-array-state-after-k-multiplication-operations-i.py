class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        minHeap = [(n, i) for i, n in enumerate(nums)]
        heapq.heapify(minHeap)
        res = nums[::]
        
        for _ in range(k):
            n, i = heapq.heappop(minHeap)
            res[i] *= multiplier
            heapq.heappush(minHeap,(res[i], i))
            
        
        return res