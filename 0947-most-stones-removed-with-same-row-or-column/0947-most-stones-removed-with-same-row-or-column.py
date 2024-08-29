class UnionFind:
    def __init__(self):
        self.parent = {}
    
    def find(self, x):
        if self.parent.setdefault(x, x) != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = UnionFind()
    
        for x, y in stones:
            uf.union(x, ~y)  # Union row with negative column to keep them in separate spaces

        # The number of connected components is the number of unique roots
        return len(stones) - len({uf.find(x) for x, y in stones})