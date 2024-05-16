# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        n = 0
        cur = head
        while cur:
            cur = cur.next
            n+=1
        for _ in range(k%n):
            cur = head
            while cur.next.next:
                cur = cur.next
            
            temp = head
            head = cur.next
            cur.next = None
            head.next = temp
        return head