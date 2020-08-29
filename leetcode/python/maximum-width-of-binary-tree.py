# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.mins = defaultdict(int)
        self.maxs = defaultdict(int)
        
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        self.calc_positions(root, 1, 1)
        return max(self.maxs[depth] - self.mins[depth] for depth in self.mins) + 1
        
    def calc_positions(self, node: TreeNode, pos: int, depth: int):
        if node is None:
            return
        
        if depth in self.mins:
            self.mins[depth] = min(pos, self.mins[depth])
        else:
            self.mins[depth] = pos
            
        if depth in self.maxs:
            self.maxs[depth] = max(pos, self.maxs[depth])
        else:
            self.maxs[depth] = pos
        
        self.calc_positions(node.left, pos * 2, depth + 1)
        self.calc_positions(node.right, pos * 2 + 1, depth + 1)
