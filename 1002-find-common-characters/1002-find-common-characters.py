class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        word1 = set(words[0])
        ans = []
        for char in word1:
            
            freq = min([word.count(char) for word in words])
            ans += [char]*freq
        
        return ans