public class Game
{
	public Queue<int> deck1 { get; set; }

	public Queue<int> deck2 { get; set; }
	public Game()
	{
		deck1 = ReadPlayerDeck();
		deck2 = ReadPlayerDeck();
	}
	public static Queue<int> ReadPlayerDeck()
	{
		var nums = new Queue<int>();
		Console.ReadLine(); // Ignore Player id part
		while (true)
		{
			var line = Console.ReadLine();
			if (string.IsNullOrEmpty(line))
			{
				break;
			}
			nums.Enqueue(int.Parse(line));
		}
		return nums;
	}

	public int Play()
	{
		while (deck1.Count > 0 && deck2.Count > 0)
		{
			var num1 = deck1.Dequeue();
			var num2 = deck2.Dequeue();
			if (num1 > num2)
			{
				deck1.Enqueue(num1);
				deck1.Enqueue(num2);
			}
			else
			{
				deck2.Enqueue(num2);
				deck2.Enqueue(num1);
			}
		}
		var winningDeck = deck1.Count > 0 ? deck1 : deck2;
		var sum = 0;
		while (winningDeck.Count > 0)
		{
			var num = winningDeck.Dequeue();
			sum += num * (winningDeck.Count + 1);
		}
		return sum;
	}
}

var game = new Game();
Console.WriteLine(game.Play())