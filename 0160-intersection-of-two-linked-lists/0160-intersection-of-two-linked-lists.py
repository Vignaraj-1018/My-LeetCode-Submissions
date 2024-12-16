# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l,r = headA, headB
        
        while l!=r:
            l = l.next if l else headB
            r = r.next if r else headA

        return l