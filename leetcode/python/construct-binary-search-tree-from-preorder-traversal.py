from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None

        node = TreeNode(preorder[0])
        pivot = 1
        while pivot < len(preorder):
            if preorder[pivot] > node.val:
                break

            pivot += 1

        left_node = self.bstFromPreorder(preorder[1:pivot])
        right_node = self.bstFromPreorder(preorder[pivot:])

        node.left = left_node
        node.right = right_node
        return node
            


def test_node(root: TreeNode, n: int) -> bool:
    maybe_sorted_list = []
    def preorder_traverse(node: TreeNode) -> None:
        if node is None:
            return

        preorder_traverse(node.left)
        maybe_sorted_list.append(node.val)
        preorder_traverse(node.right)

    preorder_traverse(root)
    if len(maybe_sorted_list) == n and maybe_sorted_list == sorted(maybe_sorted_list):
        return True

    return False


if __name__ == "__main__":
    solver = Solution()
    test_input = [8,5,1,7,10,12]
    node = solver.bstFromPreorder(test_input)
    assert test_node(node, len(test_input))
