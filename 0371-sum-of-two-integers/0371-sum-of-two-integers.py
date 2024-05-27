class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX_INT = 0xFFFFFFFF

        while MAX_INT & b:
            carry = (a & b) << 1

            a = a ^ b
            b = carry
        return a & MAX_INT if b > 0 else a