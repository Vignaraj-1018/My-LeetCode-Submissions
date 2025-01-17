class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        last = 0

        for i in derived:
            if i:
                last = ~last
        
        return 0 == last