nums = [1,2,0,1]

nums= list(set(nums))
nums.sort()
print(nums)

length=[]
cur=1
for i in range(0,len(nums)-1):
    print(nums[i],nums[i+1],end='')
    if nums[i]+1==nums[i+1]:
        cur+=1
        print("yes")
    else:
        length.append(cur)
        cur=1
        print("no")

length.append(cur)

print(length)