class Solution:
    def countAndSay(self, n: int) -> str:
        
        def rle(term):
            result = []
            i = 0
            while i < len(term):
                count = 1
                while i + 1 < len(term) and term[i] == term[i + 1]:
                    i += 1
                    count += 1
                result.append(str(count) + term[i])
                i += 1
            return ''.join(result)
        
        current_term = "1"
        for _ in range(1, n):
            current_term = rle(current_term)

        return current_term