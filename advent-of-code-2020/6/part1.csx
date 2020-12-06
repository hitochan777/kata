var sum = 0;
var set = new HashSet<char>();
while (true)
{
    var line = Console.ReadLine();
    if (line == null)
    {
        break;
    }
    set.UnionWith(line);
    if (line.Length == 0)
    {
        sum += set.Count;
        set = new HashSet<char>();
    }
}
sum += set.Count; // add last chunk

Console.WriteLine(sum);