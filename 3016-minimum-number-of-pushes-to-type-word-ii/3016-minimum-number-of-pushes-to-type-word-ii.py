class Solution:
    def minimumPushes(self, word: str) -> int:
        
        count = Counter(word)
        res = 0
        k = 0
        for c in sorted(count, key = lambda x: count[x], reverse = True):
            res += count[c] * (1 + k // 8 )
            k += 1
        return res