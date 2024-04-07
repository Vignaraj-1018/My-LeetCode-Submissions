height = [1,8,6,2,5,4,8,3,7]

l=0
r=len(height)-1

_max=0

while l<r:
    _max = max(min(height[l],height[r])*(r-l),_max)
    if height[l]<height[r]:
        l+=1
    else:
        r-=1

print(_max)