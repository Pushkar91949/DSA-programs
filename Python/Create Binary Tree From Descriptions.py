# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        node_map = {}
        children = set()
        for par,child,isleft in descriptions:
            isleft = bool(isleft)

            if par not in node_map:
                node_map[par] = TreeNode(par)
            if child not in node_map:
                node_map[child] = TreeNode(child)
            
            if isleft:
                node_map[par].left = node_map[child]
            else:
                node_map[par].right = node_map[child]

            children.add(child)
        for node in node_map.values():
            if node.val not in children:
                return node
        return None
