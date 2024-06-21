class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
    
        base = 0
        for i in range(n):
            if grumpy[i] == 0:
                base += customers[i]

        maxCus = 0
        cus = 0

        
        for i in range(n):
            if grumpy[i] == 1:
                cus += customers[i]
            if i >= minutes:
                if grumpy[i - minutes] == 1:
                    cus -= customers[i - minutes]

            maxCus = max(maxCus, cus)

        return base + maxCus