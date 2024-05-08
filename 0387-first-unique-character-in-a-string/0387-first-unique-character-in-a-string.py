class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for i in s:
            if i not in count:
                count[i]=1
            else:
                count[i] +=1
        print(count)
        for c in count:
            if count[c]==1:
                return s.index(c)
        return -1