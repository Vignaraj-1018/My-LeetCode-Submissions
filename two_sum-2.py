nums = [2,7,11,15]
target = 9

l = 0
r = len(nums)-1

while l<r:
    if nums[l] + nums[r] >target:
        r-=1
    elif nums[l] + nums[r] <target:
        l+=1
    else:
        break

print(l,r)