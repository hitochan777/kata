var sum = 0;
var set = new HashSet<char>();
var isFirst = true;
while (true)
{
    var line = Console.ReadLine();
    if (string.IsNullOrEmpty(line))
    {
        sum += set.Count;
        set = new HashSet<char>();
        if (line == null)
        {
            break;
        }
        isFirst = true;
        continue;
    }

    if (isFirst)
    {
        set.UnionWith(line);
        isFirst = false;
    }
    else
    {
        set.IntersectWith(line);
    }
}

Console.WriteLine(sum);