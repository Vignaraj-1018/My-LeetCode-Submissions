class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX_INT = 0xFFFFFFFF

        while MAX_INT & b:
            xor = a ^ b
            carry = (a & b) << 1

            a = xor
            b = carry
        print(a, b)
        return a & MAX_INT if b > 0 else a