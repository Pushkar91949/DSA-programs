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
    public int getDecimalValue(ListNode head) {
        List<Integer> binary = new ArrayList<>();
        while (head != null) {
            binary.add(head.val);
            head = head.next;
        }
        
        int ans = 0;
        Collections.reverse(binary);
        
        for (int i = 0; i < binary.size(); i++) {
            int bit = binary.get(i);
            ans += bit * (int) Math.pow(2, i);
        }
        return ans;
    }
}
