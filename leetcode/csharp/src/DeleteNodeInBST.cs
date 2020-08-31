namespace src
{
	public class DeleteNodeInBST
	{
		private (TreeNode, TreeNode) FindNode(TreeNode node, int key, TreeNode parent)
		{
			if (node == null)
			{
				return (null, null);
			}

			if (node.val == key)
			{
				return (node, parent);
			}

			if (node.val > key)
			{
				return FindNode(node.left, key, node);
			}

			return FindNode(node.right, key, node);
		}

		private (TreeNode, TreeNode) FindMinimum(TreeNode node, TreeNode parent)
		{
			if (node == null)
			{
				return (null, null);
			}

			if (node.left == null)
			{
				return (node, parent);
			}

			return FindMinimum(node.left, node);
		}

		private TreeNode DeleteNode(TreeNode node, int key, TreeNode parent)
		{
			var (target, targetParent) = FindNode(node, key, parent);
			if (target == null)
			{
				return node;
			}

			if (target.left == null && target.right == null)
			{
				if (targetParent.left == target)
				{
					targetParent.left = null;
				}
				else
				{
					targetParent.right = null;
				}

				return parent;
			}

			if (target.left == null || target.right == null)
			{
				var nonEmptyChild = target.left ?? target.right;
				if (targetParent.left == target)
				{
					targetParent.left = nonEmptyChild;
				}
				else
				{
					targetParent.right = nonEmptyChild;
				}

				return parent;
			}

			var (minTarget, minTargetParent) = FindMinimum(node.right, parent);
			DeleteNode(node, minTarget.val, parent);
			minTarget.left = node.left;
			minTarget.right = node.right;
			if (parent.left == node)
			{
				parent.left = minTarget;
			}
			else
			{
				parent.right = minTarget;
			}

			return parent;
		}

		public TreeNode DeleteNode(TreeNode root, int key)
		{
			var dummyRoot = new TreeNode {left = root};
			return DeleteNode(root, key, dummyRoot).left;
		}
	}
}
