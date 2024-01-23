# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head == None or head.next == None:
            return head
        
        length = ListNode()
        
        ans = ListNode()
        begin = ListNode

        length = head
        begin = head
        ans = head

        l = 0 
        while length != None:
            length = length.next
            l+=1
        
        k %= l

        if k == 0:
            return head
        count = 1 
        while head != None:
            if count + k == l:
                sample = head.next
                ans = sample
                head.next = None

                while sample.next:
                    sample = sample.next
                
                sample.next = begin
                count+=1

            else:
                head=head.next
                count += 1
        return ans  
        
