var validCount = 0;
while (true)
{
    var line = Console.ReadLine();
    if (line == null)
    {
        break;
    }
    var tokens = line.Split(' ');
    var positions = tokens[0].Split("-");
    var firstPos = int.Parse(positions[0]);
    var secondPos = int.Parse(positions[1]);
    var targetChar = tokens[1][0];
    var password = tokens[2];
    if ((password[firstPos - 1] == targetChar) != (password[secondPos - 1] == targetChar))
    {
        validCount++;
    }
}
Console.WriteLine(validCount);