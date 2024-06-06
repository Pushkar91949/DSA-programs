#class Node:
#    def __init__(self, data):
#        self.data = data
#        self.next = None


# your task is to complete this function
# function should return true/false or 1/0
def isCircular(head):
    # Code here
    traveller = head
    traveller = traveller.next
    while traveller:
        if traveller == head:
            return True
        traveller = traveller.next
    return False
  # Question link: https://www.geeksforgeeks.org/problems/circular-linked-list/1
