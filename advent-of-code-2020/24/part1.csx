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
Console.WriteLine(manager.CountBlackTiles());