class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        
        n = len(books)
        cache = {}
        def helper(i):
            if i == n:
                return 0
            if i in cache:
                return cache[i]
            
            max_height = 0
            cur_width = shelfWidth
            cache[i] = float('inf')
            
            for j in range(i, n):
                
                width, height = books[j]
                
                if cur_width < width:
                    break
                
                max_height = max(max_height, height)
                cur_width -= width
                
                cache[i] = min(cache[i], helper(j + 1) + max_height)
            
            return cache[i]
        return helper(0)