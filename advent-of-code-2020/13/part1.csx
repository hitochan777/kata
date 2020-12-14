var earliest = int.Parse(Console.ReadLine());
var target = Console.ReadLine().Split(',').Where(s => s != "x").Select(s => { var id = int.Parse(s); return new { diff = id - earliest % id, id }; }).OrderBy(x => x.diff).First();
Console.WriteLine(target.diff * target.id);
