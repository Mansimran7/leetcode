# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # Floyd Warshall's Algorithm (slow rabbit / fast rabbit)
        # Time complexity O(N)

        if not head:
            return False

        slow = head
        if head.next:
            fast = head.next 
        else:
            return False

        while(fast != slow):
            if slow.next:
                slow = slow.next
            else:
                False
            if fast.next and fast.next.next:
                fast = fast.next.next
            else:
                return False
        return True
        
