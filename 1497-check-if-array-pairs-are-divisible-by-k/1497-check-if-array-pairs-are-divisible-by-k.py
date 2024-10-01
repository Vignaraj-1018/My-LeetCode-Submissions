class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder_count = defaultdict(int)
    
        for num in arr:
            remainder = num % k
            remainder_count[remainder] += 1

        for remainder in remainder_count:
            if remainder == 0:
                if remainder_count[remainder] % 2 != 0:
                    return False
            elif remainder_count[remainder] != remainder_count[k - remainder]:
                    return False

        return True