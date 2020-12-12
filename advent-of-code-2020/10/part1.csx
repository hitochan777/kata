var nums = new List<int> { 0 };
while (true)
{
	var line = Console.ReadLine();
	if (line == null)
	{
		break;
	}
	var num = int.Parse(line);
	nums.Add(num);
}
nums.Sort();
var oneCount = 0;
var threeCount = 1;
for (int i = 1; i < nums.Count; i++)
{
	var diff = nums[i] - nums[i - 1];
	if (diff == 1)
	{
		oneCount++;
	}
	if (diff == 3)
	{
		threeCount++;
	}
}
Console.WriteLine(oneCount);
Console.WriteLine(threeCount);
Console.WriteLine(oneCount * threeCount);