public static class IdCalculator
{
    static public int CalcId(string str)
    {
        return Convert.ToInt32(str.Replace("F", "0").Replace("B", "1").Replace("L", "0").Replace("R", "1"), 2);
    }
}

var maxId = 0;

while (true)
{
    var line = Console.ReadLine();
    if (line == null)
    {
        break;
    }
    var id = IdCalculator.CalcId(line);
    maxId = Math.Max(id, maxId);
}

Console.WriteLine(maxId);