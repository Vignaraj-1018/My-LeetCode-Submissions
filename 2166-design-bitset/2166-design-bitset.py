class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.bits = 0 
        self.count_ones = 0
        self.flipped_bits = (1 << size) - 1

    def fix(self, idx: int) -> None:
        if not (self.bits & (1 << idx)):
            self.bits |= (1 << idx)
            self.count_ones += 1

    def unfix(self, idx: int) -> None:
        if self.bits & (1 << idx):
            self.bits &= ~(1 << idx)
            self.count_ones -= 1

    def flip(self) -> None:
        self.bits ^= self.flipped_bits
        self.count_ones = self.size - self.count_ones

    def all(self) -> bool:
        return self.count_ones == self.size

    def one(self) -> bool:
        return self.count_ones > 0

    def count(self) -> int:
        return self.count_ones

    def toString(self) -> str:
        result = []
        for i in range(self.size):
            if self.bits & (1 << i):
                result.append('1')
            else:
                result.append('0')
        return ''.join(result)

        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()