# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None or head.next == None:
            return head
        
        ans = ListNode()
        dummy = ListNode()
        ans.val = 101
        ans.next = head 
        dummy = ans
        while ans != None:
            if not ans.next or not ans.next.next:
                ans = ans.next
            elif ans.next.val == ans.next.next.val:
                target = ans.next.val 
                prev = ans
                prev = prev.next
                while(prev and prev.val == target):
                    prev=prev.next
                ans.next = prev
            else:
                ans = ans.next

        return dummy.next
