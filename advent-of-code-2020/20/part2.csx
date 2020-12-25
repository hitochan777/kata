#r "System.Text.RegularExpressions"

using System.Text.RegularExpressions;
public class DefaultDictionary<TKey, TValue> : Dictionary<TKey, TValue>
{
	public new TValue this[TKey key]
	{
		get
		{
			TValue val;
			if (!TryGetValue(key, out val))
			{
				return default(TValue);
			}
			return val;
		}
		set { base[key] = value; }
	}
}

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

	public Tile FilpVert()
	{
		return new Tile { Id = Id, Rows = Rows.Reverse().ToArray() };
	}
	public Tile FilpHoriz()
	{
		return new Tile { Id = Id, Rows = Rows.Select(row => row.Reverse().ToArray()).ToArray() };
	}
	public Tile Rotate()
	{
		var n = Rows.Length;
		var rotated = Enumerable.Range(0, n).Select(i => Enumerable.Range(0, n).Select(j => Rows[n - j - 1][i]).ToArray()).ToArray();
		return new Tile { Id = Id, Rows = rotated };
	}
	public Tile Rotate(int n)
	{
		var tile = this;
		for (var i = 0; i < n; i++)
		{
			tile = tile.Rotate();
		}
		return tile;
	}
	public IEnumerable<Tile> EnumTransformations()
	{
		for (var i = 0; i <= 3; i++)
		{
			var rotated = Rotate(i);
			yield return rotated;
			var vertFlipped = rotated.FilpVert();
			yield return vertFlipped;
			var horizFlipped = rotated.FilpHoriz();
			yield return horizFlipped;
			var vertHorizFlipped = rotated.FilpVert().FilpHoriz();
			yield return vertHorizFlipped;
		}
	}
	public bool IsMatchRight(Tile tile)
	{
		return this.GetEdge(Side.Right) == tile.GetEdge(Side.Left);
	}
	public bool IsMatchBottom(Tile tile)
	{
		return this.GetEdge(Side.Bottom) == tile.GetEdge(Side.Top);
	}
	public Tile ConcatHoriz(Tile tile)
	{
		var concated = new List<char[]>();
		var n = this.Rows.Length;
		for (var i = 0; i < n; i++)
		{
			concated.Add((new string(this.Rows[i].ToArray()) + new string(tile.Rows[i].ToArray())).ToCharArray());
		}
		return new Tile { Id = 0, Rows = concated.ToArray() };
	}
	public Tile ConcatVert(Tile tile)
	{
		return new Tile { Id = 0, Rows = this.Rows.Concat(tile.Rows.ToArray()).ToArray() };
	}
	public int FindPattern(List<string> pattern)
	{
		var count = 0;
		for (var i = 0; i <= Rows.Length - pattern.Count; i++)
		{
			var matches = Regex.Matches(new string(Rows[i]), pattern[0]);
			foreach (Match match in matches)
			{
				var tempCount = match.Value.Count(c => c == '#');

				var valid = true;
				for (var p = 1; p < pattern.Count; p++)
				{
					var matched = Regex.IsMatch(new string(Rows[i + p]).Substring(match.Index, pattern[p].Length), pattern[p]);
					if (!matched)
					{
						valid = false;
						break;
					}
					tempCount += new string(Rows[i + p]).Substring(match.Index, pattern[p].Length).Count(c => c == '#');
				}
				if (valid)
				{
					Console.WriteLine(i);
					Console.WriteLine(match.Value);
					for (var p = 1; p < pattern.Count; p++)
					{
						Console.WriteLine(new string(Rows[i + p]).Substring(match.Index, pattern[p].Length));
					}
					Console.WriteLine("");
					count += tempCount;
				}
			}
		}
		return count;
	}
	public Tile RemoveBorder()
	{
		return new Tile { Id = 0, Rows = Rows.Skip(1).SkipLast(1).Select(row => row.Skip(1).SkipLast(1).ToArray()).ToArray() };
	}
	public override string ToString()
	{
		return Id + "\n" + string.Join('\n', Rows.Select(row => new string(row)));
	}
}

var tiles = new HashSet<Tile>();
var edgeCount = new DefaultDictionary<string, int>();
while (true)
{
	var maybeTile = Tile.ReadTile();
	if (maybeTile == null)
	{
		break;
	}
	var top = maybeTile.GetEdge(Side.Top);
	var reversedTop = new string(top.Reverse().ToArray());
	var right = maybeTile.GetEdge(Side.Right);
	var reversedRight = new string(right.Reverse().ToArray());
	var bottom = maybeTile.GetEdge(Side.Bottom);
	var reversedBottom = new string(bottom.Reverse().ToArray());
	var left = maybeTile.GetEdge(Side.Left);
	var reversedLeft = new string(left.Reverse().ToArray());

	edgeCount[top]++;
	edgeCount[right]++;
	edgeCount[bottom]++;
	edgeCount[left]++;
	edgeCount[reversedTop]++;
	edgeCount[reversedRight]++;
	edgeCount[reversedBottom]++;
	edgeCount[reversedLeft]++;
	tiles.Add(maybeTile);
}

Tile cornerTile = null;

foreach (var tile in tiles)
{
	var top = edgeCount[tile.GetEdge(Side.Top)];
	var right = edgeCount[tile.GetEdge(Side.Right)];
	var bottom = edgeCount[tile.GetEdge(Side.Bottom)];
	var left = edgeCount[tile.GetEdge(Side.Left)];
	if (top + right + bottom + left == 6)
	{
		cornerTile = tile;
		if (right == 1)
		{
			cornerTile = cornerTile.FilpHoriz();
		}
		if (bottom == 1)
		{
			cornerTile = cornerTile.FilpVert();
		}
		tiles.Remove(tile);
		break;
	}
}

var restored = new List<List<Tile>> { new List<Tile> { cornerTile } };

while (tiles.Count > 0)
{
	foreach (var tile in tiles)
	{

		var prev = restored.Count == 1 ? restored[0][^1] : restored[^2][restored[^1].Count];
		var matchingTile = tile.EnumTransformations().Where(transformed =>
		{
			if (restored.Count == 1)
			{
				return restored[0][^1].IsMatchRight(transformed);
			}
			return restored[^2][restored[^1].Count].IsMatchBottom(transformed);
		}).FirstOrDefault();
		if (matchingTile != null)
		{
			restored[^1].Add(matchingTile);
			if (restored[^1].Count == 3)
			{
				restored.Add(new List<Tile>());
			}
			tiles.Remove(tile);
			break;
		}
	}
}
restored.RemoveAt(restored.Count - 1);

Tile transformedRestoredImage = null;

foreach (var row in restored)
{
	var concated = row[0].RemoveBorder();
	for (var i = 1; i < row.Count; i++)
	{
		concated = concated.ConcatHoriz(row[i].RemoveBorder());
	}
	if (transformedRestoredImage == null)
	{
		transformedRestoredImage = concated;
	}
	else
	{
		transformedRestoredImage = transformedRestoredImage.ConcatVert(concated);
	}
}

var pattern = new List<string> {
	@"..................#.",
	@"#....##....##....###",
	@".#..#..#..#..#..#..."
};

// foreach (var image in transformedRestoredImage.EnumTransformations()) {
// 	Console.WriteLine(image);
// }

Console.WriteLine(transformedRestoredImage);
var restoredImage = transformedRestoredImage.EnumTransformations().Where(transformation => transformation.FindPattern(pattern) > 0).FirstOrDefault();
var count = restoredImage.FindPattern(pattern);

Console.WriteLine(restoredImage);
Console.WriteLine(count);
Console.WriteLine(restoredImage.ToString().Count(c => c == '#') - count);