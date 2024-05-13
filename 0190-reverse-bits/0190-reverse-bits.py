class Solution:
    def reverseBits(self, n: int) -> int:
        n = f'{n:032b}'
        return int(n[::-1],2)
