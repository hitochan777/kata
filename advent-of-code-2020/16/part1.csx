#r "System.Text.RegularExpressions"

using System.Text.RegularExpressions;

public class FieldRule
{
	public List<RangeRule> RangeRules { get; set; }
	public bool IsValid(int value)
	{
		return RangeRules.Any(rule => rule.IsInRange(value));
	}

    public override string ToString() {
        return string.Join(" or ", RangeRules);
    }
}
public class RangeRule
{
	public int Min { get; set; }
	public int Max { get; set; }

	public bool IsInRange(int value)
	{
		return value >= Min && value <= Max;
	}
    public override string ToString() {
        return $"{Min}-{Max}";
    }

}
public class TicketChecker
{
	public List<FieldRule> ParseRules()
	{
		var fieldRules = new List<FieldRule>();
		var rx = new Regex(@"^.+: (?<rule>\d+-\d+)( or (?<rule>\d+-\d+))*$", RegexOptions.Compiled);
		while (true)
		{
			var line = Console.ReadLine();
			if (string.IsNullOrEmpty(line))
			{
				break;
			}
			var match = rx.Matches(line).FirstOrDefault();
			var rangeRules = match.Groups["rule"].Captures.Select(
				rule =>
				{
					var splitted = rule.Value.Split("-");
					return new RangeRule { Min = int.Parse(splitted[0]), Max = int.Parse(splitted[1]) };
				}
			).ToList();
			fieldRules.Add(new FieldRule { RangeRules = rangeRules });
		}
		return fieldRules;
	}

	public void ParseYourTicket()
	{
		Console.ReadLine();
		Console.ReadLine();
		Console.ReadLine();
	}

	public List<List<int>> ParseNearbyTicket()
	{
		Console.ReadLine();
		var result = new List<List<int>>();
		while (true)
		{
			var line = Console.ReadLine();
			if (line == null)
			{
				return result;
			}
			result.Add(line.Split(",").Select(val => int.Parse(val)).ToList());
		}
	}

	public int GetTotalInvalidValues(List<List<int>> lists, List<FieldRule> rules)
	{
		var sum = 0;
		foreach (var list in lists)
		{
			for (int i = 0; i < list.Count; i++)
			{
                var isValid = rules.Any(rule => rule.IsValid(list[i]));
				if (!isValid)
				{
					sum += list[i];
				}
			}
		}
		return sum;
	}
}

var checker = new TicketChecker();
var rules = checker.ParseRules();
checker.ParseYourTicket();
var nearbyTickets = checker.ParseNearbyTicket();
var total = checker.GetTotalInvalidValues(nearbyTickets, rules);
Console.WriteLine(total);