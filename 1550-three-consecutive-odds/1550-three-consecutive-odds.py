class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n1, n2, n3 = 0, 1, 2

        while n3 < len(arr):
            if arr[n1] % 2 and arr[n2] % 2 and arr[n3] % 2:
                return True
            
            n1 += 1
            n2 += 1
            n3 += 1
            
        return False