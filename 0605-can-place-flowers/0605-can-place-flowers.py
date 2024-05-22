class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        res = False
        m = len(flowerbed)
        if n==0:
            return True
        if m==1 and flowerbed[0]==-0:
            return True
        elif m==1 and flowerbed[0]==0:
            return False
        for i in range(m):
            if flowerbed[i]==0 and (i-1>0 and flowerbed[i-1]==0) and (i+1<m and flowerbed[i+1]==0):
                n-=1
                flowerbed[i]=1
            if i==0 and flowerbed[i]==0 and flowerbed[i+1]==0:
                n-=1
                flowerbed[i]=1
            if i==m-1 and flowerbed[i]==0 and flowerbed[i-1]==0:
                n-=1
                flowerbed[i]=1
            if n==0:
                return True
        return False