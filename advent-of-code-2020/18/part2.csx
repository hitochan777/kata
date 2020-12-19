public static class ExpressionEvaluator
{
	public static Dictionary<string, int> Priority = new Dictionary<string, int>{
		{"(", -1},
		{"*", 0} ,
		{"+", 1},
	};
	public static List<string> Tokenize(string expression)
	{
		var tokens = new List<string>();
		var cur = new StringBuilder();
		foreach (var ch in expression)
		{
			if (char.IsDigit(ch))
			{
				cur.Append(ch);
			}
			else
			{
				if (cur.Length > 0)
				{
					tokens.Add(cur.ToString());
				}
				cur.Clear();
				if (ch != ' ')
				{
					tokens.Add($"{ch}");
				}
			}
		}
		if (cur.Length > 0)
		{
			tokens.Add(cur.ToString());
		}
		return tokens;
	}

	public static long Evaluate(string expression)
	{
		var tokens = Tokenize(expression);
		var valueStack = new Stack<long>();
		var opStack = new Stack<string>();
		Action evaluateArithmeticOp = () =>
		{
			var op = opStack.Pop();
			var a = valueStack.Pop();
			var b = valueStack.Pop();
			var result = op == "+" ? a + b : a * b;
			valueStack.Push(result);
		};
		foreach (var token in tokens)
		{
			var isValue = long.TryParse(token, out long value);
			if (isValue)
			{
				valueStack.Push(value);
			}
			else if (token == "(")
			{
				opStack.Push(token);
			}
			else if (token == ")")
			{
				while (opStack.Count > 0 && opStack.Peek() != "(")
				{
					evaluateArithmeticOp();
				}
				opStack.Pop();
			}
			else
			{
				while (opStack.Count > 0 && Priority[opStack.Peek()] >= Priority[token])
				{
					evaluateArithmeticOp();
				}
				opStack.Push(token);
			}
		}
		while (opStack.Count > 0)
		{
			evaluateArithmeticOp();
		}
		return valueStack.Peek();
	}
}

var sum = 0L;
while (true)
{
	var line = Console.ReadLine();
	if (string.IsNullOrEmpty(line))
	{
		break;
	}
	long result = ExpressionEvaluator.Evaluate(line);
	Console.WriteLine($"{line} = {result}");
	sum += result;
}

Console.WriteLine($"sum = {sum}");