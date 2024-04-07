nums = [3,2,4]
target = 6

for i in range(len(nums)):
    for j in range(i,len(nums)):
        if nums[i] + nums[j] == target:
            print(i,j)