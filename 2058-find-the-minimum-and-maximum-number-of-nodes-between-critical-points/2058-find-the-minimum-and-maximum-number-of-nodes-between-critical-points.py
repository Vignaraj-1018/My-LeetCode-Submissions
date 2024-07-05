# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev, cur = head, head.next
        nxt = cur.next
        
        min_dist, max_dist = float('inf'), -1

        first_idx, cur_idx, idx = 0, 0, 1

        while nxt:

            if (prev.val < cur.val > nxt.val) or (prev.val > cur.val < nxt.val):
                if first_idx:
                    max_dist = idx - first_idx
                    min_dist = min(min_dist, idx - prev_idx)
                else:
                    first_idx = idx

                prev_idx = idx

            prev, cur, nxt = cur, nxt, nxt.next
            idx += 1

        if min_dist == float('inf'):
            min_dist = -1

        return [min_dist, max_dist]