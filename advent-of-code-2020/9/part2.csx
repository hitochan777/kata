var TARGET = 393911906;
var lines = new List<long>();
while (true) {
    var line = Console.ReadLine();
    if (line == null) {
        break;
    }
    lines.Add(long.Parse(line));
}

for (var i = 0; i < lines.Count; i++) {
    var sum = lines[i];
    var min = lines[i];
    var max = lines[i];
    for (var j = i + 1; j < lines.Count; j++) {
        Console.WriteLine($"{lines[i]} {lines[j]}");
        if (sum > TARGET) {
            break;
        }
        if (sum == TARGET) {
            Console.WriteLine($"{min} {max}");
            return;
        }
        sum += lines[i];
        min = Math.Min(min, lines[i]);
        max = Math.Max(max, lines[i]);
    }
}