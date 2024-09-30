class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize
        self.n = 0

    def push(self, x: int) -> None:
        if self.n == self.maxSize:
            return
        self.stack.append(x)
        self.n += 1

    def pop(self) -> int:
        if self.n == 0:
            return -1
        self.n -= 1
        return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        if k > self.n:
            k = self.n
        for i in range(k):
            self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)