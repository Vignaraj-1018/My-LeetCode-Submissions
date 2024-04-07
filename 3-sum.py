nums = [-1,0,1,2,-1,-4]

res= []
nums.sort()

if nums[0]>=0:
    print([])

for i, a in enumerate(nums):
    if i>0 and a == nums[i-1]:
        continue

    l,r = i+1, len(nums)-1
    while l<r:
        three_sum = a + nums[l] + nums[r]
        if three_sum >0:
            r-=1
        elif three_sum <0:
            l+=1
        else:
            res.append([a,nums[l],nums[r]])
            l+=1
            while l<r and nums[l]==nums[l-1]:
                l+=1

print(res)