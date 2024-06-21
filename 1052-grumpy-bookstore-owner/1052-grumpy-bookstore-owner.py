class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
    
        base_satisfied = 0
        for i in range(n):
            if grumpy[i] == 0:
                base_satisfied += customers[i]

        max_additional_satisfied = 0
        current_additional_satisfied = 0

        
        for i in range(n):
            if grumpy[i] == 1:
                current_additional_satisfied += customers[i]
            if i >= minutes:
                if grumpy[i - minutes] == 1:
                    current_additional_satisfied -= customers[i - minutes]

            max_additional_satisfied = max(max_additional_satisfied, current_additional_satisfied)

        return base_satisfied + max_additional_satisfied