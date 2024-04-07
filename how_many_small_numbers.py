num = [8,1,2,2,3]

sorted_num = sorted(num)

print(sorted_num)

for i in range(len(num)):
    num[i] = sorted_num.index(num[i])

print(num)