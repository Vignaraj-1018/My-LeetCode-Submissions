nums=[1,2,3,1]

count = {}

for i in nums:
    if i not in count:
        count[i] = 1
    else:
        print(False)
        count[i] += 1

print(count)