class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        n = len(graph)
        rev_graph = [ [] for _ in range(n) ]
        indegree = [0] * n
        
        for i in range(n):
            for it in graph[i]:
                rev_graph[it].append(i) 
                indegree[i] += 1
                
        
        q = []
        safe = []
        for i in range(n):
            if not indegree[i]:
                q.append(i)
                
        
        while q:
            
            cur = q.pop(0)
            safe.append(cur)
            
            for i in rev_graph[cur]:
                indegree[i] -= 1
                if not indegree[i]:
                    q.append(i)
        
        return sorted(safe)