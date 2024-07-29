class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        n = len(rating)
        res = 0
        for m in range(1, n - 1):
            left_smaller = right_larger = 0
            for i in range(m):
                if rating[i] < rating[m]:
                    left_smaller += 1
            
            for i in range(m + 1, n):
                if rating[i] > rating[m]:
                    right_larger += 1
            
            res += left_smaller * right_larger

            left_larger = m - left_smaller
            right_smaller = n - m - 1 - right_larger

            res += left_larger * right_smaller
        
        return res