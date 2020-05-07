class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        x_depth, x_parent = self.find(root, x, 0, None)
        y_depth, y_parent = self.find(root, y, 0, None)
        return x_depth == y_depth and x_parent is not y_parent
        
    def find(self, node: TreeNode, target: int, depth: int, parent: TreeNode):
        if node is None:
            return -1, None
        
        if node.val == target:
            return (depth, parent)
    
        left_depth, left_parent = self.find(node.left, target, depth + 1, node)
        right_depth, right_parent = self.find(node.right, target, depth + 1, node)
        return (left_depth, left_parent) if left_depth >= 0 else (right_depth, right_parent)
