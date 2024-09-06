# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        ptr = dummy
        nums = set(nums)
        while ptr and ptr.next:
            if ptr.next.val in nums:
                ptr.next = ptr.next.next
            else:
                ptr = ptr.next
        return dummy.next

  # Question link: https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/
