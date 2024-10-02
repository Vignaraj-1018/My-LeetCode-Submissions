class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        num_index = defaultdict(list)
        min_heap = []
        
        for i in range(len(arr)):
            num_index[arr[i]].append(i)
        
        for num in num_index:
            heapq.heappush(min_heap, num)
        
        rank = 1
        res = [0 for _ in range(len(arr))]
        while min_heap:
            
            cur = heapq.heappop(min_heap)
            for i in num_index[cur]:
                res[i] = rank
            
            rank += 1
        
        return res