var ship = (x: 0f, y: 0f);
var wp = (x: 10f, y: 1f);

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
			wp.y += value;
			break;
		case 'E':
			wp.x += value;
			break;
		case 'W':
			wp.x -= value;
			break;
		case 'S':
			wp.y -= value;
			break;
		case 'L':
		case 'R':
			var sign = cmd == 'L' ? 1.0 : -1.0;
			var cos = Math.Cos(sign * value * Math.PI / 180);
			var sin = Math.Sin(sign * value * Math.PI / 180);
			wp = ((float)(wp.x * cos - wp.y * sin), (float)(wp.x * sin + wp.y * cos));
			break;
		case 'F':
			ship.x += wp.x * value;
			ship.y += wp.y * value;
			break;
	}
	Console.WriteLine($"{line} waypoint = ({wp.x}, {wp.y}), ship = ({ship.x}, {ship.y})");
}

Console.WriteLine($"{Math.Abs(ship.x)} + {Math.Abs(ship.y)} = {Math.Abs(ship.x) + Math.Abs(ship.y)}");