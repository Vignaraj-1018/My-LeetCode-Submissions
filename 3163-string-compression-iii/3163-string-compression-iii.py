class Solution:
    def compressedString(self, word: str) -> str:
        segments = ""
        cur = [0, word[0]]

        for c in word:
            if c == cur[1]:
                if cur[0] < 9:
                    cur[0] += 1
                else:
                    segments += f"9{cur[1]}"
                    cur = [1, c]
            else:
                segments += f"{cur[0]}{cur[1]}"
                cur = [1, c]
        
        segments += f"{cur[0]}{cur[1]}"
        return segments