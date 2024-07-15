/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode createBinaryTree(int[][] descriptions) {
        Map<Integer, TreeNode> nodeMap = new HashMap<>();
        Set<Integer> children = new HashSet<>();

        for (int[] desc: descriptions) {
            int par = desc[0];
            int child = desc[1];
            boolean isLeft = desc[2] == 1;

            if (!nodeMap.containsKey(par)) {
                nodeMap.put(par, new TreeNode(par));
            }
            if (!nodeMap.containsKey(child)) {
                nodeMap.put(child, new TreeNode(child));
            }
            if (isLeft) {
                nodeMap.get(par).left = nodeMap.get(child);
            } else {
                nodeMap.get(par).right = nodeMap.get(child);
            }

            children.add(child);
        }
        for (int key : nodeMap.keySet()) {
            if (!children.contains(key)) {
                return nodeMap.get(key);
            }
        }
        return null;
    }
}
