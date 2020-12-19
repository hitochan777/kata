class ConwayCubeSimulator
{
	public (int start, int end) XRange { get; set; }
	public (int start, int end) YRange { get; set; }
	public (int start, int end) ZRange { get; set; } = (0, 0);
	public Dictionary<(int x, int y, int z), bool> Map { get; set; } = new Dictionary<(int x, int y, int z), bool>();

	private int CountActiveNeighbors((int x, int y, int z) coord)
	{
		var activeCount = 0;
		for (int dx = -1; dx <= 1; dx++)
		{
			for (int dy = -1; dy <= 1; dy++)
			{
				for (int dz = -1; dz <= 1; dz++)
				{
					if (dx == 0 && dy == 0 && dz == 0)
					{
						continue;
					}
					var neighbor = (coord.x + dx, coord.y + dy, coord.z + dz);
					Map.TryGetValue(neighbor, out bool isActive);
					activeCount += isActive ? 1 : 0;
				}
			}
		}
		return activeCount;
	}

	private bool GetNextState((int x, int y, int z) coord)
	{
		var activeCount = CountActiveNeighbors(coord);
		Map.TryGetValue(coord, out bool isActive);
		if (isActive)
		{
			if (activeCount == 2 || activeCount == 3)
			{
				return true;
			}
			return false;
		}
		else if (activeCount == 3)
		{
			return true;
		}
		return false;
	}

	public void ForwardStep()
	{
		XRange = (XRange.start - 1, XRange.end + 1);
		YRange = (YRange.start - 1, YRange.end + 1);
		ZRange = (ZRange.start - 1, ZRange.end + 1);
		var nextMap = new Dictionary<(int x, int y, int z), bool>();
		for (int i = XRange.start; i <= XRange.end; i++)
		{
			for (int j = YRange.start; j <= YRange.end; j++)
			{
				for (int k = ZRange.start; k <= ZRange.end; k++)
				{
					var nextState = GetNextState((i, j, k));
					nextMap[(i, j, k)] = nextState;
				}
			}
		}
		Map = nextMap;
	}

    public int CountActive() {
        return Map.Values.Where(isActive => isActive).Count();
    }

	public override string ToString()
	{
		var sb = new StringBuilder();
		for (int k = ZRange.start; k <= ZRange.end; k++)
		{
			sb.AppendLine($"z = {k}");
			for (int i = XRange.start; i <= XRange.end; i++)
			{
				for (int j = YRange.start; j <= YRange.end; j++)
				{
					Map.TryGetValue((i, j, k), out bool isActive);
					sb.Append(isActive ? '#' : '.');
				}
				sb.Append('\n');
			}
			sb.Append('\n');
		}
		return sb.ToString();
	}
}
var x = 0;
var y = 0;
var map = new Dictionary<(int x, int y, int z), bool>();
while (true)
{
	var line = Console.ReadLine();
	if (string.IsNullOrEmpty(line))
	{
		break;
	}
	for (var i = 0; i < line.Length; i++)
	{
		map[(x, i, 0)] = line[i] == '#';
	}
	x++;
	y = line.Length;
}

var simulator = new ConwayCubeSimulator
{
	Map = map,
	XRange = (0, x - 1),
	YRange = (0, y - 1)
};


Console.WriteLine(simulator);
for (int step = 0; step < 6; step++)
{
	simulator.ForwardStep();
    Console.WriteLine($"After {step + 1} cycle");
	Console.WriteLine(simulator);
}


Console.WriteLine($"{simulator.CountActive()} are acitve");