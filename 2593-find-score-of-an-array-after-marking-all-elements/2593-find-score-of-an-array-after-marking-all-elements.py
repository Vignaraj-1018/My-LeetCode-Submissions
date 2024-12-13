class Solution:
    def findScore(self, nums: List[int]) -> int:
        
        _nums = [(n, i) for i, n in enumerate(nums)]
        heapq.heapify(_nums)
        
        n = len(nums)
        res = 0
        marked = set()
        
        
        while _nums:
            cur, i = heapq.heappop(_nums)
            
            if i not in marked:
                res += cur
                marked.add(i)
                marked.add(i - 1)
                marked.add(i + 1)
        
        return res