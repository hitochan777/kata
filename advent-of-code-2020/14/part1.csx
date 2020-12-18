#r "System.Text.RegularExpressions"

using System.Text.RegularExpressions;

class MemoryManager
{
	public Dictionary<long, long> Memory { get; } = new Dictionary<long, long>();
	public string Mask { get; set; } = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX";

	public MemoryManager() { }

	public void AssignValue(long addr, long value)
	{
		var result = new StringBuilder();
		var binarySeq = new string(Convert.ToString(value, 2).TakeLast(36).ToArray()).PadLeft(36, '0');
		var masked = Convert.ToInt64(new string(binarySeq.Select((bit, i) => Mask[i] == 'X' ? bit : Mask[i]).ToArray()), 2);
		Memory[addr] = masked;
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
	Console.WriteLine(line);
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