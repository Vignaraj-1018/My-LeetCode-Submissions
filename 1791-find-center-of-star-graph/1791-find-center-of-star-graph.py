class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        count = []
        
        
        for e in edges:
            if e[0] in count:
                return e[0]
            if e[1] in count:
                return e[1]
            count.append(e[0])           
            count.append(e[1])
            