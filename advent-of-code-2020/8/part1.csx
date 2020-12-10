var lines = new List<(string, int, bool)>();
while (true) {
    var line = Console.ReadLine();
    if (line == null) {
        break;
    }
    var splitted = line.Split(' ');
    var op = splitted[0];
    var value = splitted[1];
    lines.Add((op, int.Parse(value), false));
}
var pc = 0;
var acc = 0;
while (true) {
    var (op, value, executed) = lines[pc];
    if (executed) {
        Console.WriteLine(acc);
        break;
    }
    lines[pc] = (op, value, true); 
    switch (op) {
        case "acc":
            acc += value;
            pc++;
            break;
        case "jmp":
            pc += value;
            break;
        case "nop":
            pc++;
            break;
    }
}