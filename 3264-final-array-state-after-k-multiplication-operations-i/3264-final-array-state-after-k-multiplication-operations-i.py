class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        minHeap = [(n, i) for i, n in enumerate(nums)]
        heapq.heapify(minHeap)
        
        
        for _ in range(k):
            n, i = heapq.heappop(minHeap)
            nums[i] *= multiplier
            heapq.heappush(minHeap,(nums[i], i))
            
        
        return nums