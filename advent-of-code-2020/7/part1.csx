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

var graph = new Dictionary<string, HashSet<string>>();

while (true)
{
    var line = Console.ReadLine();
    if (line == null)
    {
        break;
    }
    var bagInfo = BagInfo.Parse(line);
    foreach (var bag in bagInfo.Bags)
    {
        if (!graph.ContainsKey(bag.Item1))
        {
            graph[bag.Item1] = new HashSet<string>();
        }
        graph[bag.Item1].Add(bagInfo.Color);
    }
}

var visited = new HashSet<string>();
var visitQueue = new Queue<string>();
visitQueue.Enqueue("shiny gold");

while (visitQueue.Count > 0)
{
    var color = visitQueue.Dequeue();
    visited.Add(color);
    if (!graph.ContainsKey(color))
    {
        continue;
    }
    var neighbors = graph[color];
    foreach (var neighbor in neighbors)
    {
        if (visited.Contains(neighbor))
        {
            continue;
        }
        visitQueue.Enqueue(neighbor);
    }
}

Console.WriteLine(visited.Count - 1);