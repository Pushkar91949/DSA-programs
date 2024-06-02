# Detect Loop in a linked list

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None


class Solution:

    # NAIVE APPROACH:

    def detectLoopNAIVE(self, head):
        if not head or not head.next:
            return False

        d = {}

        n = head
        while n:
            if n in d.keys():
                return True
            else:
                d[n] = 1
            n = n.next
        return False

        # T.C. = O(n^2)
        # S.C. = O(n)

    # OPTIMAL APPROACH

    def detectLoopOPTIMAL(self, head):
        if not head or not head.next:
            return False

        slow = head
        fast = head

        while (fast and fast.next):
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

        return False

    # T.C. = O(n)
    # S.C. = O(1)
