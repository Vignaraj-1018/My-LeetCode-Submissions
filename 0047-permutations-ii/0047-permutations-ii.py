class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        path = []

        count = {n:0  for n in nums}

        for i in nums:
            count[i] += 1

        def dfs():

            if len(path) == len(nums):
                res.append(path.copy())
                return 

            for n in count:
                if count[n] > 0:
                    path.append(n)
                    count[n]-=1

                    dfs()

                    path.pop()
                    count[n]+=1
        
        dfs()

        return res