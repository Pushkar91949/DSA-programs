class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        # code here
        if not head or not head.next:
            return head
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                slow = head
                if slow == fast:
                    while fast.next != slow:
                        fast = fast.next
                else:
                    while slow.next != fast.next:
                        slow = slow.next
                        fast = fast.next
                fast.next = None     
                return
    # Question link: https://www.geeksforgeeks.org/problems/remove-loop-in-linked-list/s
