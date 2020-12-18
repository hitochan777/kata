#r "System.Text.RegularExpressions"

using System.Text.RegularExpressions;

class MemoryManager
{
	public Dictionary<long, long> Memory { get; } = new Dictionary<long, long>();
	public string Mask { get; set; } = "000000000000000000000000000000000000";

	public MemoryManager() { }

	public void AssignValue(long addr, long value)
	{
		foreach (var maskedAddr in ComputeTargetAddresses(addr))
		{
			// Console.WriteLine($"mem[{maskedAddr}] = {value}");
			Memory[maskedAddr] = value;
		}
	}
	public IEnumerable<long> ComputeTargetAddresses(long addr)
	{
		var binarySeq = new string(Convert.ToString(addr, 2).TakeLast(36).ToArray()).PadLeft(36, '0');
		var masked = new string(binarySeq.Select((bit, i) => Mask[i] switch
		{
			'1' => '1',
			'X' => 'X',
			_ => bit
		}).ToArray());

		foreach (var targetAddr in EnumerateCombinations(masked))
		{
			yield return Convert.ToInt64(targetAddr, 2);
		}
	}
	private IEnumerable<string> EnumerateCombinations(string masked)
	{
		if (masked.Length == 0)
		{
			yield return "";
			yield break;
		}
		var partialCombinations = EnumerateCombinations(masked.Substring(1));
		var firstChars = masked[0] == 'X' ? new List<char> { '0', '1' } : new List<char> { masked[0] };
		foreach (var firstChar in firstChars)
		{
			foreach (var partialCombination in partialCombinations)
			{
				yield return $"{firstChar}{partialCombination}";
			}
		}
	}
}

var maskRegex = new Regex(@"^mask = (?<mask>.+)$", RegexOptions.Compiled);
var memRegex = new Regex(@"^mem\[(?<addr>\d+)\] = (?<value>\d+)$", RegexOptions.Compiled);
var memoryManager = new MemoryManager();
while (true)
{
	var line = Console.ReadLine();
	if (line == null)
	{
		break;
	}
	var maskMatch = maskRegex.Matches(line).FirstOrDefault();
	if (maskMatch != null)
	{
		memoryManager.Mask = maskMatch.Groups["mask"].Value;
		continue;
	}
	// otherwise it should be memory assignment
	var memMatch = memRegex.Matches(line).FirstOrDefault();
	if (memMatch == null)
	{
		throw new Exception("mem matche failed");
	}
	var addr = long.Parse(memMatch.Groups["addr"].Value);
	var value = long.Parse(memMatch.Groups["value"].Value);
	memoryManager.AssignValue(addr, value);
}

Console.WriteLine(memoryManager.Memory.Values.Sum());