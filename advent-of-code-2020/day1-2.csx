var nums = new List<int>();
while (true)
{
    var line = Console.ReadLine();
    if (line == null)
    {
        break;
    }
    nums.Add(int.Parse(line));
}
for (int i = 0; i < nums.Count; i++)
{
    for (int j = i + 1; j < nums.Count; j++)
    {
        for (int k = j + 1; k < nums.Count; k++)
        {
            if (nums[i] + nums[j] + nums[k] == 2020)
            {
                Console.WriteLine($"{nums[i]} * {nums[j]} * {nums[k]} = {nums[i] * nums[j] * nums[k]}");
            }
        }
    }
}

