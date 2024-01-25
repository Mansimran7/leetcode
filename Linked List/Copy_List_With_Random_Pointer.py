"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if head == None:
            return None
        curr = head 
        while curr:
            new_node = Node(curr.val, curr.next)
            curr.next = new_node
            curr = new_node.next

        curr = head 

        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next    

        old_head = head 
        curr_old = head
        new_head = head.next
        curr_new = head.next
        while old_head:
            
            old_head = old_head.next.next
            if old_head:
                curr_new.next = old_head.next 
            else:
                curr_new.next = None
            cur_old = curr_old.next
            curr_new = curr_new.next
        
        return new_head
        

            
