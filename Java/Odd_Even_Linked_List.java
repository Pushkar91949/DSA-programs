/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode oddEvenList(ListNode head) {
        if (head == null || head.next == null){
            return head;
        }
        ListNode l = head;
        ListNode r = head.next;
        
        ListNode temp = r;
        
        while (r != null && r.next != null){
            l.next = r.next;
            l = l.next;
            r.next = l.next;
            r = r.next;
        }
        l.next = temp;
        return head;
    }
}
// Question link: https://leetcode.com/problems/odd-even-linked-list/
