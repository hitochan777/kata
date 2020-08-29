# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        odd_head, even_head = head, head.next
        odd_tail, even_tail = head, head.next
        
        p, i = head.next.next, 1
        while p is not None:
            if i % 2 == 0:
                even_tail.next = p
                even_tail = p
                
            else:
                odd_tail.next = p
                odd_tail = p
                
            p = p.next
            i += 1
            
        odd_tail.next = even_head
        even_tail.next = None
        return odd_head
