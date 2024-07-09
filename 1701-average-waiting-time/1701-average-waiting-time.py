class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        t, total = 0, 0

        for arr, order in customers:
            if t > arr:
                total += t - arr
            else:
                t = arr
            
            t += order
            total += order
        
        return total / len(customers)