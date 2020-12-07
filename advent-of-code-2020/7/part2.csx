// clear crimson bags contain 3 pale aqua bags, 4 plaid magenta bags, 3 dotted beige bags, 3 dotted black bags.

public class BagInfo
{
    public string Color { get; set; }
    public IList<(string, int)> Bags { get; set; }

    public static BagInfo Parse(string str)
    {
        var splitted = str.Split("contain");
        var color = string.Join(" ", splitted[0].Trim().Split(' ').SkipLast(1));
        var bags = splitted[1].Trim().Split(",").Select(partRaw =>
        {
            var parts = partRaw.Trim().Split(' ');
            if (parts.First() == "no")
            {
                return (null, 0);
            }
            var color = string.Join(" ", parts.Skip(1).SkipLast(1));
            var quantity = int.Parse(parts.First());
            return (color, quantity);
        }).Where(bag => bag.color != null).ToList();
        return new BagInfo { Color = color, Bags = bags };
    }
}

var graph = new Dictionary<string, HashSet<(string, int)>>();

while (true)
{
    var line = Console.ReadLine();
    if (line == null)
    {
        break;
    }
    var bagInfo = BagInfo.Parse(line);
    graph[bagInfo.Color] = new HashSet<(string, int)>(bagInfo.Bags);
}

var total = 0;
var visitQueue = new Queue<(string, int)>();
visitQueue.Enqueue(("shiny gold", 1));

while (visitQueue.Count > 0)
{
    var color = visitQueue.Dequeue();
    if (!graph.ContainsKey(color.Item1))
    {
        continue;
    }
    var neighbors = graph[color.Item1];
    foreach (var neighbor in neighbors)
    {
        var delta = neighbor.Item2 * color.Item2;
        total += delta;
        visitQueue.Enqueue((neighbor.Item1, delta));
    }
}

Console.WriteLine(total);