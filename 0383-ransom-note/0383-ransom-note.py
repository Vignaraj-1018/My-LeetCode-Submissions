class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countA = {}
        countB = {}
        
        for i in ransomNote:
            countA[i] = countA.get(i, 0) + 1
            
        for i in magazine:
            countB[i] = countB.get(i, 0) + 1
            
        print(countA, countB)
        
        for c in countA:
            # print(c, countA[c], countB[c])
            if c not in countB:
                return False
            if c in countB and countA[c] > countB[c]:
                return False
        return True