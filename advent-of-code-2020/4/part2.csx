using System.Text.RegularExpressions;
public static class PassportReader
{
    static string[] requiredKeys = { "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid" };

    private static bool isStringNumberAndBetween(string maybeVal, int min, int max)
    {
        if (int.TryParse(maybeVal, out int result))
        {
            return result >= min && result <= max;
        }
        return false;
    }
    private static bool isValid(string key, string value)
    {
        if (key == "byr")
        {
            return isStringNumberAndBetween(value, 1920, 2002);
        }
        if (key == "iyr")
        {
            return isStringNumberAndBetween(value, 2010, 2020);
        }
        if (key == "eyr")
        {
            return isStringNumberAndBetween(value, 2020, 2030);
        }
        if (key == "hgt")
        {
            var rx = new Regex(@"^(?<value>\d+)(?<unit>(cm|in))$", RegexOptions.Compiled);
            var matches = rx.Matches(value);
            if (matches.Count != 1)
            {
                return false;
            }
            var match = matches[0];
            var unit = match.Groups["unit"].Value;
            var val = match.Groups["value"].Value;
            if (unit == "cm")
            {
                return isStringNumberAndBetween(val, 150, 193);
            }
            return isStringNumberAndBetween(val, 59, 76);
        }
        if (key == "hcl")
        {
            var rx = new Regex(@"^#[0-9a-f]{6}$", RegexOptions.Compiled);
            var matches = rx.Matches(value);
            return matches.Count == 1;
        }
        if (key == "ecl")
        {
            return value == "amb" || value == "blu" || value == "brn" || value == "gry" || value == "grn" || value == "hzl" || value == "oth";
        }
        if (key == "pid")
        {
            var rx = new Regex(@"^[0-9]{9}$", RegexOptions.Compiled);
            var matches = rx.Matches(value);
            return matches.Count == 1;
        }
        if (key == "cid")
        {
            return true;
        }
        return false;
    }
    public static bool? CheckPasssport()
    {
        var keys = new HashSet<string>();
        var line = Console.ReadLine();
        if (line == null)
        {
            return null;
        }
        while (!string.IsNullOrEmpty(line))
        {
            var pairs = line.Split(' ');
            foreach (var pair in pairs)
            {
                var splitted = pair.Split(":");
                var key = splitted[0];
                var value = splitted[1];
                if (isValid(key, value))
                {
                    keys.Add(key);
                }
            }
            line = Console.ReadLine();
        }
        foreach (var requiredKey in requiredKeys)
        {
            if (!keys.Contains(requiredKey))
            {
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