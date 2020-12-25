public enum Side
{
	Top,
	Right,
	Bottom,
	Left,
}
public class Tile
{
	public char[][] Rows { get; set; }
	public int Id { get; set; }
	public string GetEdge(Side side)
	{
		switch (side)
		{
			case Side.Top:
				return new string(Rows[0]);
			case Side.Right:
				return new string(Rows.Select(row => row[^1]).ToArray());
			case Side.Bottom:
				return new string(Rows[^1]);
			case Side.Left:
				return new string(Rows.Select(row => row[0]).ToArray());
			default:
				throw new ArgumentException($"Invalid side {side}");
		}
	}
	public static Tile ReadTile()
	{
		var idStr = Console.ReadLine();
		if (string.IsNullOrEmpty(idStr))
		{
			return null;
		}
		var id = new string(idStr.Split(" ").Last().SkipLast(1).ToArray());
		var rows = new List<char[]>();
		while (true)
		{
			var line = Console.ReadLine();
			if (string.IsNullOrEmpty(line))
			{
				break;
			}
			var chars = line.ToArray();
			rows.Add(chars);
		}
		return new Tile { Id = int.Parse(id), Rows = rows.ToArray() };
	}
	public override string ToString()
	{
		return Id + "\n" + string.Join('\n', Rows.Select(row => new string(row)));
	}
}

var tiles = new List<Tile>();
var edgeCount = new Dictionary<string, int>();
while (true)
{
	var maybeTile = Tile.ReadTile();
	if (maybeTile == null)
	{
		break;
	}
	var top = maybeTile.GetEdge(Side.Top);
	var right = maybeTile.GetEdge(Side.Right);
	var bottom = maybeTile.GetEdge(Side.Bottom);
	var left = maybeTile.GetEdge(Side.Left);
	if (!edgeCount.ContainsKey(top))
	{
		edgeCount[top] = 0;
	}
	if (!edgeCount.ContainsKey(right))
	{
		edgeCount[right] = 0;
	}
	if (!edgeCount.ContainsKey(bottom))
	{
		edgeCount[bottom] = 0;
	}
	if (!edgeCount.ContainsKey(left))
	{
		edgeCount[left] = 0;
	}
	edgeCount[top]++;
	edgeCount[right]++;
	edgeCount[bottom]++;
	edgeCount[left]++;
	tiles.Add(maybeTile);
    Console.WriteLine(maybeTile);
}

var sum = 0;
foreach (var tile in tiles)
{
	var top = edgeCount[tile.GetEdge(Side.Top)];
	var right = edgeCount[tile.GetEdge(Side.Right)];
	var bottom = edgeCount[tile.GetEdge(Side.Bottom)];
	var left = edgeCount[tile.GetEdge(Side.Left)];
	if (top == 1 && right == 1)
	{
		sum += tile.Id;
		Console.WriteLine(tile.Id);
	}
	if (right == 1 && bottom == 1)
	{
		sum += tile.Id;
		Console.WriteLine(tile.Id);
	}
	if (bottom == 1 && left == 1)
	{
		sum += tile.Id;
		Console.WriteLine(tile.Id);
	}
	if (left == 1 && top == 1)
	{
		sum += tile.Id;
		Console.WriteLine(tile.Id);
	}
}

Console.WriteLine(sum);
