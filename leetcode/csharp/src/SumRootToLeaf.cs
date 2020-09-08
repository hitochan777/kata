using System;

namespace src
{
	public class Solution
	{
		public int SumRootToLeaf(TreeNode node, string current)
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
			return SumRootToLeaf(node.left, binSeq) + SumRootToLeaf(node.right, binSeq);
		}
		public int SumRootToLeaf(TreeNode root)
		{
			return SumRootToLeaf(root, "");
		}
	}
}
