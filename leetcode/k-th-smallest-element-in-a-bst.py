# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_sorted_list(self, node: TreeNode):
        if node is None:
            return []
        
        left_list = self.get_sorted_list(node.left)
        right_list = self.get_sorted_list(node.right)
        return left_list + [node.val] + right_list
        
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        sorted_list = self.get_sorted_list(root)
        return sorted_list[k-1]
