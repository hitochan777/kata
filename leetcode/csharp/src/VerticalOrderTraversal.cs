public class Solution {
	private void mergeDictionary(Dictionary<int, IList<int>> a, Dictionary<int, IList<int>> b) {
		foreach (var item in b) {
			if (a.ContainsKey(item.Key)){
				a[item.Key] = a[item.Key].Concat(item.Value).ToList();
			} else {
				a[item.Key] = item.Value;
			}
		}
	}
	
	private Dictionary<int, IList<int>> traversal(TreeNode node, int index) {
		if (node == null) {
			return new Dictionary<int, IList<int>>();
		}
		var dict = new Dictionary<int, IList<int>>()
		  {
			{ index, new List<int> {node.val}}
		  };
		var leftDict = traversal(node.left, index - 1);
		var rightDict = traversal(node.right, index + 1);
		mergeDictionary(dict, leftDict);
		mergeDictionary(dict, rightDict);
		return dict;
	}
    public IList<IList<int>> VerticalTraversal(TreeNode root) {
       	var dict = traversal(root, 0);
		var keys = dict.Keys.ToList();
		keys.Sort();
		IList<IList<int>> result = new List<IList<int>> {};
		foreach (var key in keys) {
			result.Add(dict[key]);
		}
		return result;
    }
}
