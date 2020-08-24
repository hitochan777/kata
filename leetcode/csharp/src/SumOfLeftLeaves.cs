namespace src
{
	public class TreeNode
	{
		public int val;
		public TreeNode left;
		public TreeNode right;

		public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null)
		{
			this.val = val;
			this.left = left;
			this.right = right;
		}
	}

	public class SumOfLeftLeaves
	{
		public int Solve(TreeNode root)
		{
			return _SumOfLeftLeaves(root, 0);
		}

		private int _SumOfLeftLeaves(TreeNode node, int kind)
		{
			if (node == null)
			{
				return 0;
			}

			if (node.left == null && node.right == null && kind == -1)
			{
				return node.val;
			}

			int left = _SumOfLeftLeaves(node.left, -1);
			int right = _SumOfLeftLeaves(node.right, 1);
			return left + right;
		}
	}
}
