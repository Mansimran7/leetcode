# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if head == None and head.next == None:
            return head
        
        l = []

        start = ListNode()
        dummy_start = start

        while head != None:
            if len(l) < k:
                l.append(head.val)
                head = head.next
            else:
                while l:
                    start.next = ListNode()
                    start = start.next
                    start.val = l[-1]
                    l.pop()
                l.append(head.val)
                head = head.next
        if len(l) < k:
            for i in l:
                start.next = ListNode()
                start = start.next
                start.val = i
        else:
            while l:
                start.next = ListNode()
                start = start.next
                start.val = l[-1]
                l.pop()

        return dummy_start.next
        
