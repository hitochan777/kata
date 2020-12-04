public static class Methods
{
    public static long CountTrees(List<string> lines, int xSlope, int ySlope)
    {
        var count = 0;
        int x = 0, y = 0;
        while (y < lines.Count)
        {
            if (lines[y][x] == '#')
            {
                count++;
            }
            x = (x + xSlope) % lines[0].Length;
            y += ySlope;
        }
        return count;
    }
}
var lines = new List<string>();
while (true)
{
    var line = Console.ReadLine();
    if (line == null)
    {
        break;
    }
    lines.Add(line);
}
var multiplication = Methods.CountTrees(lines, 1, 1) * Methods.CountTrees(lines, 3, 1) * Methods.CountTrees(lines, 5, 1) * Methods.CountTrees(lines, 7, 1) * Methods.CountTrees(lines, 1, 2);
Console.WriteLine(multiplication);