var x = 0;
var y = 0;
var direction = 1;
var directions = new List<(int, int)> { (0, -1), (1, 0), (0, 1), (-1, 0) };
while (true)
{
	var line = Console.ReadLine();
	if (line == null)
	{
		break;
	}
	var cmd = line[0];
	var value = int.Parse(new string(line.Skip(1).ToArray()));
	switch (cmd)
	{
		case 'N':
			y -= value;
			break;
		case 'E':
			x += value;
			break;
		case 'W':
			x -= value;
			break;
		case 'S':
			y += value;
			break;
		case 'L':
			direction = (direction - value / 90 + 4) % 4;
			break;
		case 'R':
			direction = (direction + value / 90) % 4;
			break;
		case 'F':
			x += directions[direction].Item1 * value;
			y += directions[direction].Item2 * value;
			break;
	}
	// Console.WriteLine($"{x} {y}");
}

Console.WriteLine(Math.Abs(x) + Math.Abs(y));