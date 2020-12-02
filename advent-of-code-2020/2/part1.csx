var validCount = 0;
while (true)
{
    var line = Console.ReadLine();
    if (line == null)
    {
        break;
    }
    var tokens = line.Split(' ');
    var minmax = tokens[0].Split("-");
    var min = int.Parse(minmax[0]);
    var max = int.Parse(minmax[1]);
    var targetChar = tokens[1][0];
    var password = tokens[2];
    var count = password.Count(ch => ch == targetChar);
    if (count >= min && count <= max) {
        validCount++;
    }
}
Console.WriteLine(validCount);