public static class ExpressionEvaluator
{
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
		foreach (var token in tokens)
		{
			var isValue = long.TryParse(token, out long value);
			if (isValue)
			{
				var notEmpty = opStack.TryPeek(out string op);
				if (notEmpty)
				{
					if (op == "+" || op == "*")
					{
						var anotherValue = valueStack.Pop();
						var result = op == "+" ? anotherValue + value : anotherValue * value;
						valueStack.Push(result);
						opStack.Pop();
					}
					else
					{
						valueStack.Push(value);
					}
				}
				else
				{
					valueStack.Push(value);
				}
			}
			else
			{
				if (token == ")")
				{
					var ok = opStack.TryPop(out string op);
					if (!ok)
					{
						throw new Exception("supposed to be some op in stack!");
					}
					if (op != "(")
					{
						throw new Exception($"expected ( but found {op}");
					}
					var notEmpty = opStack.TryPeek(out op);
					if (notEmpty)
					{
						if (op == "+" || op == "*")
						{
							var a = valueStack.Pop();
							var b = valueStack.Pop();
							var result = op == "+" ? a + b : a * b;
							valueStack.Push(result);
							opStack.Pop();
						}
					}
				}
				else
				{
					opStack.Push(token);
				}
			}
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