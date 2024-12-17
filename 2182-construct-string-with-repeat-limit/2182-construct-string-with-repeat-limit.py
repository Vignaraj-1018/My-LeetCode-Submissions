class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        count = defaultdict(int)
        maxHeap = []
        
        for c in s:
            count[c] += 1

        for c in count:
            cur = ord(c) - ord('a') + 1
            heapq.heappush(maxHeap, (-cur, count[c]))
            
        res = ''
        
        while maxHeap:
            cur, n = heapq.heappop(maxHeap)
            cur = -cur
            if n <= repeatLimit:
                res += chr(cur + ord('a') - 1) * n
            else:
                res += chr(cur + ord('a') - 1) * repeatLimit
                if not maxHeap:
                    break
                cur2, n2 = heapq.heappop(maxHeap)
                cur2 = -cur2
                res += chr(cur2 + ord('a') - 1)
                heapq.heappush(maxHeap, (-cur, n - repeatLimit))
                if n2 - 1:
                    heapq.heappush(maxHeap, (-cur2, n2 - 1))
        return res