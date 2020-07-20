/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode RemoveElements(ListNode head, int val) {
        var prev = new ListNode(0, head);
        var root = prev;
        var p = head;
        while (p != null) {
            if (p.val == val) {
                prev.next = p.next;
            }
            else {
                prev = p;
            }
            p = p.next;
        }
        return root.next;
    }
}
