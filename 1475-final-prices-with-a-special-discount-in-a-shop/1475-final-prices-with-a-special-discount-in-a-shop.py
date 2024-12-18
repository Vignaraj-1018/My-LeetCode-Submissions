class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = prices[::]
        
        stack = []
        
        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                j = stack.pop()
                res[j] -= prices[i]
            
            stack.append(i)
            
        return res