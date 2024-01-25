# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        if head == None or head.next == None:
            return head

        start = None
        end = None

        while head != None:
            if head.val < x:
                if start == None:
                    start = ListNode()
                    dummy_start = start
                else:
                    start.next = ListNode()
                    start = start.next
                start.val = head.val
            else:
                if end == None:
                    end = ListNode()
                    dummy_end = end
                else:
                    end.next = ListNode()
                    end = end.next
                end.val = head.val
            head = head.next
        
        if start == None:
            return dummy_end
        if end == None:
            return dummy_start

        start.next = dummy_end
        return dummy_start
