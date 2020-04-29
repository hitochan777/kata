class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        self_max = self._maxPathSumPassingNode(root)
        left_max = self.maxPathSum(root.left)
        right_max = self.maxPathSum(root.right)
        print(left_max, right_max, self_max)
        
        return max(left_max, right_max, self_max)
            
    def _maxPathSumPassingNode(self, node: TreeNode) -> int:
        if node is None:
            return 0
        
        return self._maxPathSumPassingNode(node.left) + self._maxPathSumPassingNode(node.right) + node.val
