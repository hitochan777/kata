public static class PassportReader
{
    static string[] requiredKeys = { "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid" };
    public static bool? CheckPasssport()
    {
        var keys = new HashSet<string>();
        var line = Console.ReadLine();
        if (line == null) {
            return null;
        }
        while (!string.IsNullOrEmpty(line))
        {
            var pairs = line.Split(' ');
            var subkeys = pairs.Select(pair => pair.Split(':')[0]).Distinct();
            foreach (var key in subkeys)
            {
                keys.Add(key);
            }
            line = Console.ReadLine();
        }
        foreach (var requiredKey in requiredKeys)
        {
            if (!keys.Contains(requiredKey))
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
    if (!result.HasValue) {
        break;
    }
    count += result.Value ? 1 : 0;
}
Console.WriteLine(count);