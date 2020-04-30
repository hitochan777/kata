class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        return self._isValidSequence(root, arr, 0)
        
    def _isValidSequence(self, node: TreeNode, arr: List[int], index: int) -> bool:
        if node is None or index >= len(arr):
            return False
        
        if node.val != arr[index]:
            return False
        
        if index == len(arr) - 1 and node.left is None and node.right is None:
            return True
        
        return self._isValidSequence(node.left, arr, index + 1) or self._isValidSequence(node.right, arr, index + 1)
