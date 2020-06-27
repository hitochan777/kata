class Solution:
        
    def sumNumbers(self, root: TreeNode) -> int:
        total = 0
        def traversal(node, val=""):
            nonlocal total
            if node is None:
                return
            
            cur = val + str(node.val)
            if node.left is None and node.right is None:
                total += int(cur)
                
            if node.left is not None:
                traversal(node.left, cur)
            
            if node.right is not None:
                traversal(node.right, cur)
        
        traversal(root, "")
        return total
