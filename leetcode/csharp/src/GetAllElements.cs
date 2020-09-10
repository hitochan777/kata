using System;
using System.Collections.Generic;
using System.Linq;

namespace src
{
	public class GetAllElements
	{
		private IList<int> PreorderTraversal(TreeNode node)
		{
			if (node == null)
			{
				return new List<int>();
			}

			var leftList = PreorderTraversal(node.left);
			var rightList = PreorderTraversal(node.right);
			return leftList.Concat(new List<int> {node.val}).Concat(rightList).ToList();
		}

		private IList<int> Merge(IList<int> list1, IList<int> list2)
		{
			int p1 = 0, p2 = 0;
			var mergedList = new List<int> { };
			while (p1 < list1.Count && p2 < list2.Count)
			{
				mergedList.Add(list1[p1] < list2[p2] ? list1[p1++] : list2[p2++]);
			}

			while (p1 < list1.Count)
			{
				mergedList.Add(list1[p1++]);
			}

			while (p2 < list2.Count)
			{
				mergedList.Add(list2[p2++]);
			}

			return mergedList;
		}

		public IList<int> Solve(TreeNode root1, TreeNode root2)
		{
			var sortedList1 = PreorderTraversal(root1);
			var sortedList2 = PreorderTraversal(root2);
			return Merge(sortedList1, sortedList2);
		}
	}
}
