namespace src
{
	public class InsertIntoBST
	{
		public TreeNode Solve(TreeNode root, int val)
		{
			var newNode = new TreeNode(val, null, null);
			if (root == null)
			{
				return newNode;
			}
			var parent = new TreeNode(val, null, null);
			var p = root;
			while (p != null)
			{
				parent = p;
				if (p.val >= val)
				{
					if (p.left == null)
					{
						p.left = newNode;
						break;
					}
					p = p.left;
				}
				else
				{
					if (p.right == null)
					{
						p.right = newNode;
						break;
					}
					p = p.right;
				}
			}
			return root;
		}
	}
}
