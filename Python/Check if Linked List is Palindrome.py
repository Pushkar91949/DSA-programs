#Function to check whether the list is palindrome.
class Solution:
    def isPalindrome(self, head):
        #code here
        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        pre = None
        while slow:
            temp = slow.next
            slow.next = pre
            pre = slow
            slow = temp
        
        l,r = head,pre
        while r:
            if l.data != r.data:
                return False
            l = l.next
            r = r.next
        return True

  # Problem Link: https://www.geeksforgeeks.org/problems/check-if-linked-list-is-pallindrome/1
