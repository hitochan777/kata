public static class InstructionCorrector
{
	public static (int, bool) FindAccIfValid(List<(string, int)> instructions)
	{
		var pc = 0;
		var acc = 0;
		var executedMap = new HashSet<int>();
		while (pc < instructions.Count)
		{
			var (op, value) = instructions[pc];
			if (executedMap.Contains(pc))
			{
				return (0, false);
			}
			executedMap.Add(pc);
			switch (op)
			{
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
		return (acc, true);
	}
}
var lines = new List<(string, int)>();
while (true)
{
	var line = Console.ReadLine();
	if (line == null)
	{
		break;
	}
	var splitted = line.Split(' ');
	var op = splitted[0];
	var value = splitted[1];
	lines.Add((op, int.Parse(value)));
}

for (int i = 0; i < lines.Count; i++) {
    if (lines[i].Item1 == "jmp") {
        lines[i] = ("nop", lines[i].Item2);
        var (acc, valid) = InstructionCorrector.FindAccIfValid(lines);
        if (valid) {
            Console.WriteLine(acc);
            return;
        }
        lines[i] = ("jmp", lines[i].Item2);
    }
    else if (lines[i].Item1 == "nop") {
        lines[i] = ("jmp", lines[i].Item2);
        var (acc, valid) = InstructionCorrector.FindAccIfValid(lines);
        if (valid) {
            Console.WriteLine(acc);
            return;
        }
        lines[i] = ("nop", lines[i].Item2);
    }
}