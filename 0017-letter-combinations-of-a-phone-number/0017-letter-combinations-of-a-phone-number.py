class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        lettersOfNumbers = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        
        res = []
        
        path = []
        
        def dfs(i):
            
            if i >= len(digits):
                res.append("".join(path))
                return 
                        
            for j in lettersOfNumbers[digits[i]]:
                path.append(j)
                dfs(i+1)
                path.pop()
        dfs(0)
        return res