class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode(0)
        d.next = head
        d = d.next
        while d and d.next:
            if d.val == d.next.val:
                d.next = d.next.next
            else:
                d = d.next
        return head
