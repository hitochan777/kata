var rows = new List<List<char>>();
while (true)
{
	var line = Console.ReadLine();
	if (line == null)
	{
		break;
	}
	rows.Add(new List<char>("." + line + "."));
}
var dummyRow = Enumerable.Repeat<char>('.', rows[0].Count).ToList();
rows.Insert(0, dummyRow);
rows.Add(dummyRow);

var n = rows.Count;
var m = rows[0].Count;

while (true)
{
	var changes = new HashSet<(int, int, char)>();
	for (var i = 1; i < n - 1; i++)
	{
		for (var j = 1; j < m - 1; j++)
		{
			if (rows[i][j] == '.')
			{
				continue;
			}
			var count = 0;
			for (var dx = -1; dx <= 1; dx++)
			{
				for (var dy = -1; dy <= 1; dy++)
				{
					if (dx == 0 && dy == 0)
					{
						continue;
					}
					if (rows[i + dx][j + dy] == '#')
					{
						count++;
					}
				}
			}
			if (rows[i][j] == 'L' && count == 0)
			{
				changes.Add((i, j, '#'));
			}
			else if (rows[i][j] == '#' && count >= 4)
			{
				changes.Add((i, j, 'L'));
			}
		}
	}
	if (changes.Count == 0)
	{
		break;
	}
	foreach (var change in changes)
	{
		var (x, y, c) = change;
		rows[x][y] = c;
	}
    // foreach (var row in rows) {
    //     Console.WriteLine(new String(row.ToArray()));
    // }
    // Console.WriteLine();
}

Console.WriteLine(rows.Sum(row => row.Count(c => c == '#')));
