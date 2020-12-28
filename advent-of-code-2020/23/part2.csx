public class Node
{
	public int Value { get; set; }
	public Node Next { get; set; }
}
public class CrabCupSimulator
{
	private List<Node> cups;
	private Node current;
	private Node oneNode;
	private int n;
	private Dictionary<int, Node> successor = new Dictionary<int, Node>();
	public CrabCupSimulator(List<int> nums)
	{
		cups = new List<Node>(nums.Select(num => new Node { Value = num }));
		n = nums.Count;
		for (var i = 0; i < n - 1; i++)
		{
			cups[i].Next = cups[i + 1];
		}
		cups[^1].Next = cups[0];
		current = cups[0];
		cups.Sort((a, b) => b.Value - a.Value);
		oneNode = cups[^1];
		for (var i = 0; i < n - 1; i++)
		{
			successor[cups[i].Value] = cups[i + 1];
		}
		successor[cups[^1].Value] = cups[0];
	}
	public void MoveOnce()
	{
		var picked = pickThree();
		var dest = findDest(picked);
		current.Next = picked[^1].Next;
		var tmp = dest.Next;
		dest.Next = picked[0];
		picked[^1].Next = tmp;
		current = current.Next;
	}
	private List<Node> pickThree()
	{
		return new List<Node> { current.Next, current.Next.Next, current.Next.Next.Next };
	}

	private Node findDest(List<Node> picked)
	{
		var dest = successor[current.Value];
		while (picked.Contains(dest))
		{
			dest = successor[dest.Value];
		}
		return dest;
	}

	public (int, int) FindTwoNumsAfterOne()
	{
		return (oneNode.Next.Value, oneNode.Next.Next.Value);
	}

	public override string ToString()
	{
		var values = new List<int>();
		var p = oneNode.Next;
		while (p.Value != 1)
		{
			values.Add(p.Value);
			p = p.Next;
		}

		return string.Join(",", values);
	}
}

var list = new List<int> { 8, 5, 3, 1, 9, 2, 6, 4, 7 };
// var list = new List<int> { 3, 8, 9, 1, 2, 5, 4, 6, 7 };

list.AddRange(Enumerable.Range(list.Max() + 1, 1000000 - list.Max()));
var sim = new CrabCupSimulator(list);
for (var i = 0; i < 10000000; i++)
{
	sim.MoveOnce();
	if ((i + 1) % 1000000 == 0)
	{
		var (num1, num2) = sim.FindTwoNumsAfterOne();
		Console.WriteLine($"{i + 1}: {num1} {num2}");
	}

}

var (num1, num2) = sim.FindTwoNumsAfterOne();
Console.WriteLine($"ans = {num1} * {num2} = {1L * num1 * num2}");
