using System.Collections.Generic;
using System.Linq;

namespace ZigzagLevelOrder
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

	public class Solution
	{
		public IList<IList<int>> ZigzagLevelOrder(TreeNode root)
		{
			if (root == null)
			{
				return new List<IList<int>>();
			}
			IList<IList<int>> list = new List<IList<int>>();
			var q = new List<TreeNode> { root };
			bool fromLeft = true;
			var nextQ = new List<TreeNode>();
			while (q.Count() > 0)
			{
				foreach (var node in q)
				{
					nextQ.Add(node.left);
					nextQ.Add(node.right);
				}
				if (!fromLeft)
				{
					q.Reverse();
				}
				list.Add(new List<int>(q.Select(node => node.val)));
				fromLeft = !fromLeft;
				q = nextQ;
				nextQ = new List<TreeNode>();
				q.RemoveAll(node => node == null);
			}
			return list;
		}
	}

}
