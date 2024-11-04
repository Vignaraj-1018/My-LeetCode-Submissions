class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        cur = [0, word[0]]
        
        for c in word:
            if cur[1] == c and cur[0] < 9:
                cur[0] += 1
            elif cur[0] == 9:
                comp += '9' + cur[1]
                cur = [1, c]
            elif cur[1] != c:
                comp += str(cur[0]) + cur[1]
                cur = [1, c]
        comp += str(cur[0]) + cur[1]
            
        
        return comp