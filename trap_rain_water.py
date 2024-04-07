height = [0,1,0,2,1,0,1,3,2,1,2,1]
if not height: print("Empty")
l,r,res = 0, len(height)-1,0
maxL,maxR = height[l], height[r]

while l<r:
    if maxL < maxR:
        l+=1
        maxL = max(maxL,height[l])
        res += maxL - height[l]
    else:
        r-=1
        maxR = max(maxR,height[r])
        res += maxR - height[r]

print(res)