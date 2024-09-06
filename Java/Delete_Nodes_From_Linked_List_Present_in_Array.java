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
    public ListNode modifiedList(int[] nums, ListNode head) {
        ListNode dummy = new ListNode();
        dummy.next = head;
        ListNode ptr = dummy;
        Set<Integer> set = new HashSet<>();
        for (int num : nums){
            set.add(num);
        }
        while (ptr != null && ptr.next != null){
            if (set.contains(ptr.next.val)){
                ptr.next = ptr.next.next;
            } else {
                ptr = ptr.next;
            }
        }
        return dummy.next;
    }
} // Question link: https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/
