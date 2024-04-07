candies = [2,3,5,1,3]
extraCandies = 3

maxCandies = max(candies)

for i in range(len(candies)):
    if candies[i] + extraCandies >= maxCandies:
        candies[i] = True
    else:
        candies[i] = False

print(candies)
print(*candies)
