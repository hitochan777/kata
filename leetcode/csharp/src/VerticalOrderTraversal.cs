public class Solution {
  public IList < IList < int >> VerticalTraversal(TreeNode root) {
    var dict = new Dictionary < int,
    List < (int Y, int val) >> ();
    var queue = new Queue < (int X, int Y, TreeNode node) > ();
    queue.Enqueue((0, 0, root));
    while (queue.Count > 0) {
      var node = queue.Dequeue();
      if (node.node == null) {
        continue;
      }
      if (!dict.ContainsKey(node.X)) {
        dict[node.X] = new List < (int Y, int val) > ();
      }
      dict[node.X].Add((node.Y, node.node.val));
      queue.Enqueue((node.X - 1, node.Y + 1, node.node.left));
      queue.Enqueue((node.X + 1, node.Y + 1, node.node.right));
    }
    var keys = dict.Keys.ToList();
    keys.Sort();
    IList < IList < int >> result = new List < IList < int >> {};
    foreach(var key in keys) {
      var list = dict[key];
      list.Sort();
      result.Add(list.Select(item =>item.val).ToList());
    }
    return result;
  }
}
