s = "codeleet"
indices = [4,5,6,7,0,2,1,3]

res_dict = {}
i=0
for ch in s:
    res_dict[indices[i]]= ch
    i+=1

res=''
for i in range(len(s)):
    res += res_dict[i]

print(res)
