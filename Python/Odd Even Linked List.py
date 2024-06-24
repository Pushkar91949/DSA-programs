# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        l = head
        r = head.next

        temp = r

        while r and r.next:
            l.next = r.next
            l = l.next
            r.next = l.next
            r = r.next
        l.next = temp
        return head
