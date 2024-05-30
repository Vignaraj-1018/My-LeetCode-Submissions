class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visitedSet = set()

        def dfs(cur):
            if cur in visitedSet:
                return False
            
            if preMap[cur] == []:
                return True
            
            visitedSet.add(cur)
            for i in preMap[cur]:
                if not dfs(i): return False

            visitedSet.remove(cur)
            preMap[cur] = []
            return True

        for i in range(numCourses):
            if not dfs(i): return False
        return True