public static class PassportReader
{
    static string[] requiredKeys = { "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid" };
    public static bool? CheckPasssport()
    {
        var pairs = new Dictionary<string, string>();
        var line = Console.ReadLine();
        if (line == null)
        {
            return null;
        }
        while (!string.IsNullOrEmpty(line))
        {
            var subpairs = line.Split(' ');
            var parsedSubPairs = subpairs.Select(pair => { 
                var splitted = pair.Split(':'); 
                return (key: splitted[0], value: splitted[1]);
                });
            foreach (var pair in parsedSubPairs)
            {
                pairs.Add(pair.key, pair.value);
            }
            line = Console.ReadLine();
        }
        foreach (var requiredKey in requiredKeys)
        {
            if (!pairs.ContainsKey(requiredKey))
            {
                Console.WriteLine($"not containing ${requiredKey}");
                return false;
            }
        }
        return true;
    }
}

var count = 0;

while (true)
{
    var result = PassportReader.CheckPasssport();
    if (!result.HasValue)
    {
        break;
    }
    count += result.Value ? 1 : 0;
}
Console.WriteLine(count);