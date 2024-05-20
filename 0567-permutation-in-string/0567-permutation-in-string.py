class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        wind = len(s1)
        l, r = 0, wind-1

        def isPermutation(s1, s2):
            # print(s1, s2)
            count_s1 = {}
            count_s2 = {}
            for i in s1:
                if i not in count_s1:
                    count_s1[i]=1
                else:
                    count_s1[i]+=1
            
            for i in s2:
                if i not in count_s2:
                    count_s2[i]=1
                else:
                    count_s2[i]+=1
            
            return count_s1 == count_s2
        while r<len(s2):
            if isPermutation(s1, s2[l:r+1]):
                return True
            r+=1
            l+=1
        
        return False
