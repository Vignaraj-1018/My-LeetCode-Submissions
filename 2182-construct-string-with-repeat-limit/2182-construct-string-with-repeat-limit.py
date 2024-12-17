class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        count = Counter(s)
        maxHeap = [(-ord(c), count[c]) for c in count]
        heapq.heapify(maxHeap)
          
        res = []
        
        while maxHeap:
            cur, n = heapq.heappop(maxHeap)
            cur = -cur
            
            if n <= repeatLimit:
                res.append(chr(cur) * n)
            else:
                res.append(chr(cur) * repeatLimit)
                if not maxHeap:
                    break
                cur2, n2 = heapq.heappop(maxHeap)
                cur2 = -cur2
                res.append(chr(cur2))
                heapq.heappush(maxHeap, (-cur, n - repeatLimit))
                if n2 - 1:
                    heapq.heappush(maxHeap, (-cur2, n2 - 1))
        
        return "".join(res)