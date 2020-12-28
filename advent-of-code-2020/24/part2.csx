public class TileManager
{
	public Dictionary<(int, int), bool> Flipped { get; set; } = new Dictionary<(int, int), bool>();
	public void FlipTile(string instruction)
	{
		var coord = GetCoord(instruction);
		if (!Flipped.ContainsKey(coord))
		{
			Flipped[coord] = true;
		}
		else
		{
			Flipped[coord] = !Flipped[coord];
		}
	}
	public int CountBlackTiles()
	{
		return Flipped.Values.Where(value => value).Count();
	}
	public bool ShouldBeBlack((int, int) coord)
	{
		var blackCount = EnumNeighbors(coord).Where(neighbor => Flipped.ContainsKey(neighbor) && Flipped[neighbor]).Count();
		if (Flipped.ContainsKey(coord) && Flipped[coord])
		{
			return blackCount == 1 || blackCount == 2;
		}
		return blackCount == 2;
	}
	private IEnumerable<(int, int)> EnumNeighbors((int x, int y) coord)
	{
		var deltas = new List<(int x, int y)> { (1, -1), (-1, -1), (-1, 1), (1, 1), (2, 0), (-2, 0) };
		foreach (var delta in deltas)
		{
			yield return (coord.x + delta.x, coord.y + delta.y);
		}
	}
	public void ProcessOneDay()
	{
		var newFlipped = new Dictionary<(int, int), bool>();
		foreach (var (coord, isBlack) in Flipped)
		{
			if (ShouldBeBlack(coord))
			{
				newFlipped[coord] = true;
			}
			if (isBlack)
			{
				foreach (var neighbor in EnumNeighbors(coord).Where(neighbor => ShouldBeBlack(neighbor)))
				{
					newFlipped[neighbor] = true;
				}
			}
		}
		Flipped = newFlipped;
	}
	private (int, int) GetCoord(string instruction)
	{
		var coord = (x: 0, y: 0);
		// e, se, sw, w, nw, and ne
		while (instruction.Length > 0)
		{
			if (instruction.StartsWith("se"))
			{
				coord.x += 1;
				coord.y -= 1;
				instruction = instruction.Substring(2);
			}
			else if (instruction.StartsWith("sw"))
			{
				coord.x -= 1;
				coord.y -= 1;
				instruction = instruction.Substring(2);
			}
			else if (instruction.StartsWith("nw"))
			{
				coord.x -= 1;
				coord.y += 1;
				instruction = instruction.Substring(2);
			}
			else if (instruction.StartsWith("ne"))
			{
				coord.x += 1;
				coord.y += 1;
				instruction = instruction.Substring(2);
			}
			else if (instruction.StartsWith("e"))
			{
				coord.x += 2;
				instruction = instruction.Substring(1);
			}
			else if (instruction.StartsWith("w"))
			{
				coord.x -= 2;
				instruction = instruction.Substring(1);
			}
		}
		return coord;
	}
}

var manager = new TileManager();

while (true)
{
	var line = Console.ReadLine();
	if (string.IsNullOrEmpty(line))
	{
		break;
	}
	manager.FlipTile(line);
}
for (var i = 0; i < 100; i++)
{
	manager.ProcessOneDay();
	Console.WriteLine($"Day {i + 1}: {manager.CountBlackTiles()}");
}
Console.WriteLine(manager.CountBlackTiles());