"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def _flatten(self, head):
        if head is None:
            return None, None
        
        p = head
        tail = None
        while p is not None:
            tail = p
            if p.child is None:
                p = p.next
            else:
                fl_head, fl_tail = self._flatten(p.child)
                p.child = None
                nxt = p.next
                p.next, fl_tail.next, fl_head.prev = fl_head, p.next, p
                if nxt is not None:
                    nxt.prev = fl_tail
                    
                p = nxt
                tail = nxt if nxt is not None else fl_tail
        
        return head, tail
        
    def flatten(self, head: 'Node') -> 'Node':
        new_head, _ = self._flatten(head)
        return new_head