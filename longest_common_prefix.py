strs = ["c","acc","ccc"]
# n = min([len(x) for x in strs])

# common=""

# if n ==0:
#     print("here")

# for i in range(n):
#     if strs[0][i] == strs[-1][i]:
#         common += strs[0][i]
#     else:
#         break

# print(common,n)

def longestCommonPrefix( strs):
    ans=""
    strs=sorted(strs)
    first_word=strs[0]
    last_word=strs[-1]
    for i in range(min(len(first_word),len(last_word))):
        if(first_word[i]!=last_word[i]):
            return ans
        ans+=first_word[i]

print(longestCommonPrefix(strs))
