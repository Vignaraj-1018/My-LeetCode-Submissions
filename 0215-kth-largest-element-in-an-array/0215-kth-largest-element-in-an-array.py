class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        res = 0
        heapq.heapify(heap)

        for i in nums:
            if len(heap) < k or heap[0] < i:
                heapq.heappush(heap, i)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]