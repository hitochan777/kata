using System;

namespace src
{
	public class sumRootToLeaft
	{
		public int Solve(TreeNode node, string current)
		{
			if (node == null)
			{
				return 0;
			}
			string binSeq = $"{current}{node.val}";
			if (node.left == null && node.right == null)
			{
				return Convert.ToInt32(binSeq, 2);
			}
			return Solve(node.left, binSeq) + Solve(node.right, binSeq);
		}
		public int SumRootToLeaf(TreeNode root)
		{
			return Solve(root, "");
		}
	}
}
