lst = [1,2,3,4]
for i in range(1,len(lst)):
    lst[i] += lst[i-1]

print(lst)