ratings = [1,2,87,87,87,2,1]

res = [1]*len(ratings)
for i in range(len(ratings)-1):
    if ratings[i] > ratings[i+1]:
        res[i] += 1

for i in range(len(ratings)-1,0,-1):
    if ratings[i] > ratings[i-1]:
        res[i] = res[i-1]+1
print(res,sum(res))