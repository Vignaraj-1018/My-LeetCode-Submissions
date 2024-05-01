class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        n = len(heights)
        
        for j in range(n):
            swapped = False
            
            for i in range(0,n-j-1):
                
                if heights[i] < heights[i+1]:
                    heights[i], heights[i+1] = heights[i+1], heights[i]
                    names[i], names[i+1] = names[i+1], names[i]
                    swapped = True
            
            if not swapped:
                break
        
        return names
                