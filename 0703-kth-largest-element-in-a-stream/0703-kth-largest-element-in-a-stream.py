class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        self.kthlargest = self.getKthlargest()

    def getKthlargest(self)-> int:
        if len(self.nums) < self.k:
            return None
        self.nums = sorted(self.nums)
        res = self.nums[len(self.nums)-self.k]
        return res
    
    def add(self, val: int) -> int:
        self.nums.append(val)
        return self.getKthlargest()

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)