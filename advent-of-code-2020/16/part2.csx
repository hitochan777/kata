#r "System.Text.RegularExpressions"

using System.Text.RegularExpressions;

public class FieldRule
{
	public int Index { get; set; }
	public List<RangeRule> RangeRules { get; set; }
	public bool IsValid(int value)
	{
		return RangeRules.Any(rule => rule.IsInRange(value));
	}

	public override string ToString()
	{
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
	public override string ToString()
	{
		return $"{Min}-{Max}";
	}

}
public class TicketChecker
{
	public List<FieldRule> ParseRules()
	{
		var fieldRules = new List<FieldRule>();
		var rx = new Regex(@"^.+: (?<rule>\d+-\d+)( or (?<rule>\d+-\d+))*$", RegexOptions.Compiled);
		var index = 0;
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
			fieldRules.Add(new FieldRule { Index = index++, RangeRules = rangeRules });
		}
		return fieldRules;
	}

	public List<int> ParseYourTicket()
	{
		Console.ReadLine();
		var line = Console.ReadLine();
		Console.ReadLine();
		return line.Split(",").Select(val => int.Parse(val)).ToList();
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
}

var checker = new TicketChecker();
var rules = checker.ParseRules();
var yourTicket = checker.ParseYourTicket();
var nearbyTickets = checker.ParseNearbyTicket();
var filteredTickets = nearbyTickets.Where(ticket => !ticket.Any(value => !rules.Any(rule => rule.IsValid(value)))).ToList();
var ruleMap = new Dictionary<int, int>();
while (ruleMap.Count < filteredTickets[0].Count)
{
	for (var i = 0; i < filteredTickets[0].Count; i++)
	{
		var validRules = rules.Where(rule => filteredTickets.All(ticket => rule.IsValid(ticket[i]))).Select(rule => rule.Index).ToList();
		if (validRules.Count == 1)
		{
			ruleMap[validRules[0]] = i;
			rules = rules.Where(rule => rule.Index != validRules[0]).ToList();
		}
	}
}

var total = Enumerable.Range(0, 6).Select(i => yourTicket[ruleMap[i]]).Aggregate(1L, (acc, x) => acc * x);
Console.WriteLine(total);