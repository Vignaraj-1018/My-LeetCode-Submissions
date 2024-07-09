class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        time = 0
        n = len(customers)
        res = 0
        while customers:
            if customers[0][0] <= time:
                time += customers[0][1]
                res += time - customers[0][0]
                customers.pop(0)
            else:
                time += 1
        
        print(res)
        return res / n