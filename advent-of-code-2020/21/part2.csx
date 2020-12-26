#r "System.Text.RegularExpressions"

using System.Text.RegularExpressions;


var regex = new Regex(@"(?<ingredient>\w+)( (?<ingredient>\w+))* \(contains (?<allergen>\w+)(, (?<allergen>\w+))*\)");

var map = new Dictionary<string, HashSet<string>>();
var ingredienCount = new Dictionary<string, int>();

while (true)
{
	var line = Console.ReadLine();
	if (string.IsNullOrEmpty(line))
	{
		break;
	}
	var matches = regex.Matches(line);
	var match = matches.FirstOrDefault();
	var ingredients = match.Groups["ingredient"].Captures.Select(capture => capture.Value).ToList();
	var allergens = match.Groups["allergen"].Captures.Select(capture => capture.Value).ToList();
	foreach (var allergen in allergens)
	{
		if (!map.ContainsKey(allergen))
		{
			map[allergen] = new HashSet<string>(ingredients);
		}
		else
		{
			map[allergen].IntersectWith(ingredients);
		}
	}
	foreach (var ingredient in ingredients)
	{
		if (!ingredienCount.ContainsKey(ingredient))
		{
			ingredienCount[ingredient] = 0;
		}
		ingredienCount[ingredient]++;
	}
}

var finalMap = new Dictionary<string, string>();

while (map.Count > 0)
{
	var ones = map.Where(pair => pair.Value.Count == 1).Select(pair => new { Allergen = pair.Key, Ingredient = pair.Value.First() }).ToList();
	foreach (var allergen in map.Keys)
	{
		map[allergen].RemoveWhere(ingredient => ones.Select(one => one.Ingredient).Contains(ingredient));
	}
	foreach (var one in ones)
	{
		finalMap[one.Allergen] = one.Ingredient;
		map.Remove(one.Allergen);
	}
}

foreach (var (allergen, ingredient) in finalMap)
{
	Console.WriteLine(allergen + ": " + ingredient);
}

// Run the command bellow to get the final answer
// $ cat test.txt | dotnet script part2.csx | sort | cut -d" " -f2 | tr '\n' ','
