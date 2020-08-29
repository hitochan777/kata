class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.max = -10**100
        
    def maxPathSum(self, root: TreeNode) -> int:
        return self._maxPathSum(root)[0]
            
    def _maxPathSum(self, node: TreeNode):
        self_max = node.val
        candidates = []
        line_candidates = [0]
        
        if node.left is not None:
            left_max, left_line_max = self._maxPathSum(node.left)
            self_max += max(0, left_line_max)
            candidates.append(left_max)
            line_candidates.append(left_line_max)
        
        if node.right is not None:
            right_max, right_line_max = self._maxPathSum(node.right)
            self_max += max(0, right_line_max)
            candidates.append(right_max)
            line_candidates.append(right_line_max)
            
        candidates.append(self_max)
            
        max_val = (max(candidates), max(line_candidates, default=0) + node.val)
        return max_val
