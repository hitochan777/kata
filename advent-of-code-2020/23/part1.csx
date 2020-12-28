public class CrabCupSimulator
{
	private List<int> cups;
	private int current;
	private int n;
	public CrabCupSimulator(List<int> nums)
	{
		cups = new List<int>(nums);
		n = nums.Count;
		current = cups[0];
	}
	public void MoveOnce()
	{
		Console.WriteLine(this);
		Console.WriteLine($"current: {current}");
		var picked = pickThree();
		Console.WriteLine($"pick up: {string.Join(", ", picked)}");
		var dest = findDest(picked);
		Console.WriteLine($"destination: {dest}");
		Console.WriteLine("");
		var destIndex = cups.FindIndex(cup => cup == dest);
		cups.InsertRange(destIndex + 1, picked);
		var nextCurrentIndex = (cups.FindIndex(cup => cup == current) + 1) % n;
		current = cups[nextCurrentIndex];
	}
	private List<int> pickThree()
	{
		var picked = new List<int>();
		var count = 3;
		var targetIndex = (cups.FindIndex(val => val == current) + 1) % cups.Count;
		while (count > 0)
		{
			picked.Add(cups[targetIndex]);
			targetIndex = (targetIndex + 1) % n;
			count--;
		}
		cups.RemoveAll(cup => picked.Contains(cup));
		return picked;
	}

	private int findDest(List<int> picked)
	{
		var dest = (current - 2 + n) % n;
		while (picked.Contains(dest + 1))
		{
			dest = (dest - 1 + n) % n;
		}
		return dest + 1;
	}

	public override string ToString()
	{
		return string.Join(",", cups);
	}
}

var sim = new CrabCupSimulator(new List<int> { 8, 5, 3, 1, 9, 2, 6, 4, 7 });
// var sim = new CrabCupSimulator(new List<int>{3,8,9,1,2,5,4,6,7});
for (var i = 0; i < 100; i++)
{
	Console.WriteLine(i + 1);
	sim.MoveOnce();
}
Console.WriteLine(sim);
