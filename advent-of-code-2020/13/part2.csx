Console.ReadLine();
var nums = Console.ReadLine().Split(",").Select((val, index) => new { val, index }).Where(x => x.val != "x").Select(x => new { index = x.index, val = long.Parse(x.val) }).ToList();
var ts = nums.First().val;
var period = nums.First().val;

for (var i = 1; i < nums.Count; i++)
{
	while ((ts + nums[i].index) % nums[i].val != 0)
	{
		ts += period;
	}
	period *= nums[i].val;
}

Console.WriteLine(ts);