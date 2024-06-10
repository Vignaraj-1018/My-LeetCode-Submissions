class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        res = 0
        for i, j in zip(heights, sorted(heights)):
            if i != j:
                res+=1
        
        return res