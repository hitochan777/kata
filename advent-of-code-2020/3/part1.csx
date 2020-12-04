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
var count = 0;
int x = 0, y = 0;
while (y < lines.Count) {
    Console.WriteLine($"{x} {y}");
    if (lines[y][x] == '#') {
        count++;
    }
    x = (x + 3) % lines[0].Length;
    y++;
}
Console.WriteLine(count);