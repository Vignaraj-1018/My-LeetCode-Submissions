class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        countOfNode = []
        
        
        for e in edges:
            if e[0] in countOfNode:
                return e[0]
            if e[1] in countOfNode:
                return e[1]
            countOfNode.append(e[0])           
            countOfNode.append(e[1])
            