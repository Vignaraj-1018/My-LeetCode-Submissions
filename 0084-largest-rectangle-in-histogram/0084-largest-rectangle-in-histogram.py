class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        
        for i,h in enumerate(heights):
            start = i
            
            while stack and stack[-1][1] > h:
                
                ind, ht = stack.pop()
                maxArea = max(maxArea, ht * (i-ind))
                
                start = ind
            
            stack.append((start, h))
            
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights)-i))
           
    
        return maxArea