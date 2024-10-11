class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        
        indexes = [i for i in range(len(times))]
        indexes.sort(key = lambda i : times[i][0])
        
        used_chairs = []
        available_chairs = [i for i in range(len(times))]
        
        for i in indexes:
            a, l = times[i]
            
            while used_chairs and used_chairs[0][0] <= a:
                leave, chair = heapq.heappop(used_chairs)
                heapq.heappush(available_chairs, chair)
                
            chair = heapq.heappop(available_chairs)
            heapq.heappush(used_chairs, (l, chair))
            
            if i == targetFriend:
                return chair