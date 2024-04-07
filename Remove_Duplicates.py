nums = [1,1,1,2,2,3]

k=1

for i in range(1,len(nums)):
    if i==1 or nums[i] != nums[i-2]:
        nums[k] = nums[i]
        k+=1
        
print(nums,k)