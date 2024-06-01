class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head):
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

        l,r = head, pre
        while r:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
        return True

def create_linked_list(elements):
    if not elements:
        return None
    head = ListNode(elements[0])
    current = head
    for val in elements[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    elements = []
    current = head
    while current:
        elements.append(current.val)
        current = current.next
    print("Linked list:", elements)

# Test cases
test_cases = [
    [1, 2, 2, 1],  # Palindrome
    [1, 2],        # Not a palindrome
    [1, 2, 3, 2, 1],  # Palindrome
    [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1],  # Palindrome
    [1,2,3,4,5],           # Not a palindrome
    []             # Empty list (Palindrome)
]

# Test the Solution
solution = Solution()
for i, elements in enumerate(test_cases):
    head = create_linked_list(elements)
    print(f"Test case {i+1}: {elements}")
    print_linked_list(head)
    result = solution.isPalindrome(head)
    print(f"Is palindrome: {result}\n")


# Classes:

# 1. ListNode Class:

# This class is used to create nodes for the linked list.
# Each node has a value (val) and a pointer to the next node (next).

# 2. Solution Class:

# This class contains a method (isPalindrome) to check if a linked list is a palindrome (i.e., it reads the same forward and backward).
# Checking if the List is a Palindrome


# The isPalindrome method works in several steps:

# 1. Finding the Middle of the List:

# We use two pointers, fast and slow, both starting at the head of the list.
# fast moves twice as fast as slow (two steps at a time while slow moves one step at a time).
# When fast reaches the end of the list, slow will be at the middle.
  
# 2. Reversing the Second Half:

# Starting from the middle (where slow is), we reverse the second half of the list.
# We use another pointer pre to help reverse the links between the nodes.
# By the end of this step, pre will point to the head of the reversed second half.

# 3. Comparing the Two Halves:

# We then set two pointers: l starting from the head of the list (beginning of the first half) and r starting from pre (beginning of the reversed second half).
# We compare the values of the nodes that l and r point to.
# If all corresponding values match, the list is a palindrome; otherwise, it is not.


