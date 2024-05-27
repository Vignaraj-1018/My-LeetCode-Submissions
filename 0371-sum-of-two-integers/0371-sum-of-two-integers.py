class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF

        while mask & b:
            xor = a ^ b
            carry = (a & b) << 1

            a = xor
            b = carry

        return a & mask if b > 0 else a