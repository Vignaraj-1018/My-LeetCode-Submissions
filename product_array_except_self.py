nums = [-1,1,0,-3,3]

result = [1]*len(nums)
left = 1
for i in range(len(nums)):
    result[i] = left
    left*= nums[i]
left=1
for i in range(len(nums)-1,-1,-1):
    result[i] *= left
    left*= nums[i]


print(result)