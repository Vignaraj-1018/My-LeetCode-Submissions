nums = [1,2,3,4,5,6,7]
k=3

k = k % len(nums)
k = k % len(nums)
overflow = nums[-k:]
nums[k:] = nums[:-k]
nums[:k] = overflow

print(nums)