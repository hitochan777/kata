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

var validStrings = new HashSet<string>(textMatcher.EnumStrings("0"));

var count = 0;
while (true)
{
	var line = Console.ReadLine();
	if (string.IsNullOrEmpty(line))
	{
		break;
	}
	if (validStrings.Contains(line))
	{
		count++;
	}
}

Console.WriteLine(count);
