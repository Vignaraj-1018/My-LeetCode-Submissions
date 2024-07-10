class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0
        for cd in logs:
            if '../' in cd and res != 0:
                res -= 1
            elif './' not in cd:
                res += 1
        return res