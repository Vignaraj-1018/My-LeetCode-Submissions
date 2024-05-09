class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        heapq.heapify(heap)
        
        for i in stones:
            heapq.heappush(heap,i*-1)
        print(heap)
        while len(heap)>1:
            a,b = heapq.heappop(heap), heapq.heappop(heap)
            c = (a*-1) - (b*-1)
            if c:
                heapq.heappush(heap,c*-1)
        if len(heap)==1:        
            return heapq.heappop(heap)*-1  
        else: return 0