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
    public int pairSum(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;
        int ans = 0;
        while (fast != null && fast.next != null){
            fast = fast.next.next;
            slow = slow.next;
        }
        ListNode cur = slow;
        ListNode pre = null;

        while (cur != null){
            ListNode next_node = cur.next;
            cur.next = pre;
            pre = cur;
            cur = next_node;
        }
        ListNode first = head;
        ListNode second = pre;

        while (second != null){
            ans = Math.max(ans,first.val+second.val);
            first = first.next;
            second = second.next;
        }
        return ans;
    }
} 
