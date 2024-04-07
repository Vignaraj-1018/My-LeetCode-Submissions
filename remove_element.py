nums = [3,2,2,3]
val=3

ind = 0
for i in range(len(nums)):
    if nums[i] !=val:
        nums[ind] = nums[i]
        ind += 1


print(nums, ind)