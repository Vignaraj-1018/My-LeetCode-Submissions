class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        def dfs(i, cur_set):
            
            if i == len(s):
                return 0
            
            res = 0
            
            for j in range(i, len(s)):
                sub = s[i:j+1]
                
                if sub in cur_set:
                    continue
                    
                cur_set.add(sub)
                res = max(res, 1 + dfs(j + 1, cur_set))
                cur_set.remove(sub)
            
            return res
            
        
        return dfs(0, set())