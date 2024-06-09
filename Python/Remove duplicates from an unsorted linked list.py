#User function Template for python3
'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	
'''
class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # code here
        # return head after editing list
        seen = set()
        seen.add(head.data)
        l = head
        while l and l.next:
            if l.next.data in seen:
                l.next = l.next.next
            else:
                seen.add(l.next.data)
                l = l.next
        return head
      # Problem link: https://www.geeksforgeeks.org/problems/remove-duplicates-from-an-unsorted-linked-list/1
