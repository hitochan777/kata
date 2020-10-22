using System.Collections.Generic;
using System.Linq;

namespace src
{
	public class MinumumDepthBinaryTree
	{
		public int MinDepth(TreeNode node)
		{
			var values = new List<int>();
			if (node == null)
			{
				return 0;
			}
			if (node.left == null && node.right == null)
			{
				return 1;
			}
			if (node.left != null)
			{
				values.Add(MinDepth(node.left) + 1);
			}
			if (node.right != null)
			{
				values.Add(MinDepth(node.right) + 1);
			}
			return values.Min();
		}
	}
}
