#r "System.Text.RegularExpressions"

using System.Text.RegularExpressions;

public class RuleNode
{
	public List<List<string>> Rules { get; set; }
	public string Value { get; set; }
}

public class TextMatcher
{
	public Dictionary<string, RuleNode> Table { get; set; }

	public List<string> EnumStrings(string ruleIndex)
	{
		if (Table[ruleIndex].Value != null)
		{
			return new List<string> { Table[ruleIndex].Value };
		}
		return Table[ruleIndex].Rules.SelectMany(subrules =>
		{
			var enumerationCollections = subrules.Select(subrule => EnumStrings(subrule).Distinct()).ToList();
			// Assume there are only one or two collections
			if (enumerationCollections.Count == 1)
			{
				return enumerationCollections[0];
			}
			else if (enumerationCollections.Count == 2)
			{
				var result = new List<string>();
				foreach (var first in enumerationCollections[0])
				{
					foreach (var second in enumerationCollections[1])
					{
						result.Add(first + second);
					}
				}

				return result;
			}
			else
			{
				throw new Exception($"{enumerationCollections.Count} child rules found");
			}
		}).ToList();
	}
}
var table = new Dictionary<string, RuleNode>();

var innodeRegex = new Regex(@"^(?<num>\d+): (?<components>(\d+)( \d+)*)( \| (?<components>(\d+)( \d+)*))*$", RegexOptions.Compiled);
var leafRegex = new Regex(@"^(?<num>\d+): ""(?<char>\w)""$", RegexOptions.Compiled);

while (true)
{
	var line = Console.ReadLine();
	if (string.IsNullOrEmpty(line))
	{
		break;
	}
	var innodeMatch = innodeRegex.Matches(line).FirstOrDefault();
	if (innodeMatch != null)
	{
		var num = innodeMatch.Groups["num"].Value;
		var components = innodeMatch.Groups["components"].Captures.Select(capture => capture.Value.Split(" ").ToList()).ToList();
		table[num] = new RuleNode
		{
			Value = null,
			Rules = components
		};
		continue;
	};

	var leafMatch = leafRegex.Matches(line).FirstOrDefault();
	if (leafMatch != null)
	{
		var num = leafMatch.Groups["num"].Value;
		table[num] = new RuleNode
		{
			Value = leafMatch.Groups["char"].Value,
			Rules = null,
		};
		continue;
	}

	throw new Exception($"no match! {line}");
}

var textMatcher = new TextMatcher
{
	Table = table
};

var validStrings42 = new HashSet<string>(textMatcher.EnumStrings("42"));
var validStrings31 = new HashSet<string>(textMatcher.EnumStrings("31"));

foreach (var str in validStrings31)
{
	Console.WriteLine(str);
}
Console.WriteLine("");

foreach (var str in validStrings42)
{
	Console.WriteLine(str);
}

var STRING_LEN = 8;

var count = 0;
while (true)
{
	var line = Console.ReadLine();
	if (string.IsNullOrEmpty(line))
	{
		break;
	}
	if (line.Length % STRING_LEN != 0 || line.Length < STRING_LEN * 2)
	{
		continue;
	}
	var state = 0;
	var isValid = true;
	var count42 = 0;
	var count31 = 0;
	for (var i = 0; i < line.Length; i += STRING_LEN)
	{
		var substr = line.Substring(i, STRING_LEN);
		switch (state)
		{
			case 0:
				if (validStrings42.Contains(substr))
				{
					state = 1;
					count42++;
				}
				else
				{
					state = -1;
					isValid = false;
				}
				break;
			case 1:
				if (validStrings42.Contains(substr))
				{
					state = 1;
					count42++;
				}
				else if (validStrings31.Contains(substr))
				{
					state = 2;
					count31++;
				}
				else
				{
					state = -1;
					isValid = false;
				}
				break;
			case 2:
				if (validStrings31.Contains(substr))
				{
					state = 2;
					count31++;
				}
				else
				{
					state = -1;
					isValid = false;
				}
				break;
		}
		if (!isValid)
		{
			break;
		}
	}
	if (state == 2 && count42 > 0 && count31 > 0 && count42 - count31 > 0)
	{
		count++;
	}
}

Console.WriteLine(count);
