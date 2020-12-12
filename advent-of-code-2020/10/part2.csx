var nums = new List<long> { 0 };
while (true)
{
	var line = Console.ReadLine();
	if (line == null)
	{
		break;
	}
	var num = long.Parse(line);
	nums.Add(num);
}
nums.Sort();
nums.Add(nums.Max() + 3);
var dp = new List<long>();
for (var i = 0; i < nums.Count + 2; i++)
{
	dp.Add(0);
}
dp[1] = 1;
dp[2] = 2;
for (var i = 3; i < nums.Count; i++)
{
	for (var j = 1; j <= 3; j++)
	{
		if (nums[i] - nums[i - j] <= 3)
		{
			dp[i] += dp[i - j];
		}
	}
}
Console.WriteLine(dp[nums.Count-1]);