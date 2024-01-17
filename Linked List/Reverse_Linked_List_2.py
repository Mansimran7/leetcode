# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode()
        ans = ListNode()

        ans = head
        dummy = head
        count = 1 
        l = []
        while head != None:
            if count >= left and count <= right:
                while(count <= right):
                    l.append(head.val)
                    head = head.next
                    count+=1
                while(l):
                    ans.val = l[-1]
                    l.pop()
                    ans = ans.next
            else:
                ans.val = head.val
                ans = ans.next
                count+=1
                head = head.next  

        return dummy
