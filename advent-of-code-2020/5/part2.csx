public static class IdCalculator
{
    static public int CalcId(string str)
    {
        return Convert.ToInt32(str.Replace("F", "0").Replace("B", "1").Replace("L", "0").Replace("R", "1"), 2);
    }
}

var maxId = 0;
var ids = new List<int>();

while (true)
{
    var line = Console.ReadLine();
    if (line == null)
    {
        break;
    }
    var id = IdCalculator.CalcId(line);
    ids.Add(id);
}
ids.Sort();

for (int i = 1; i < ids.Count - 1; i++) {
    if (ids[i] - 1 != ids[i-1]) {
        Console.WriteLine(ids[i] - 1);
        break;
    } 
    if ( ids[i] + 1 != ids[i+1]) {
        Console.WriteLine(ids[i] + 1);
        break;
    }
}