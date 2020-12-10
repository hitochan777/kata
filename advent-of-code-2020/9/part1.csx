var WINDOW = 25;
var lines = new List<long>();
while (true) {
    var line = Console.ReadLine();
    if (line == null) {
        break;
    }
    lines.Add(long.Parse(line));
}
for (var i = WINDOW; i < lines.Count; i++) {
    var target = lines[i];
    var valid = false;
    for (var j = i - WINDOW; j < i - 1; j++) {
        for (var k = j + 1; k < i; k++) {
            if (lines[j] == lines[k]) {
                continue;
            }
            if (lines[j] + lines[k] == target) {
                valid = true;
                break;
            }
        }
        if (valid) {
            break;
        }
    }
    if (!valid) {
        Console.WriteLine(lines[i]);
        break;
    }
}