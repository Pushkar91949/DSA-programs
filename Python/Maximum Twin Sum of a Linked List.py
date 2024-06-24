# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        ans = 0

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        cur = slow
        pre = None

        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node

        first = head
        second = pre

        while second:
            ans = max(ans, first.val + second.val)
            first = first.next
            second = second.next

        return ans
