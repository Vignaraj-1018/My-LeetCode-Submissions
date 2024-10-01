class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder_count = defaultdict(int)
    
        # Count the remainders when dividing elements by k
        for num in arr:
            remainder = num % k
            remainder_count[remainder] += 1

        # Check for valid pairs
        for remainder in remainder_count:
            if remainder == 0:
                # For remainder 0, we need an even count
                if remainder_count[remainder] % 2 != 0:
                    return False
            else:
                # For other remainders, check if count(remainder) == count(k - remainder)
                if remainder_count[remainder] != remainder_count[k - remainder]:
                    return False

        return True