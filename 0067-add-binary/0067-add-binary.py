class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        s = ''
        carry = 0
        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += 1 if a[i] == '1' else 0
                i -= 1
            if j >= 0:
                carry += 1 if b[j] == '1' else 0
                j -= 1
            s = s + ('1' if (carry % 2) else '0')
            carry //= 2

        return s[::-1]