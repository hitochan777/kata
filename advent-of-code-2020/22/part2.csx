#r "System.Collections"

using System.Collections;

public class Game
{
	public Queue<int> Deck1 { get; set; }

	public Queue<int> Deck2 { get; set; }
	public HashSet<(string, string)> PreviousDecks { get; set; } = new HashSet<(string, string)>();
	public Game() { }

	public static Game CreateGameFromStdin()
	{
		var Deck1 = ReadPlayerDeck();
		var Deck2 = ReadPlayerDeck();
		return new Game { Deck1 = Deck1, Deck2 = Deck2 };
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
		while (Deck1.Count > 0 && Deck2.Count > 0)
		{
			if (PreviousDecks.Contains((string.Join(',', Deck1), string.Join(',', Deck2))))
			{
				return 1;
			}
			var winner = 0;
			Deck1.GetHashCode();
			PreviousDecks.Add((string.Join(',', Deck1), string.Join(',', Deck2)));
			var num1 = Deck1.Dequeue();
			var num2 = Deck2.Dequeue();
			if (Deck1.Count >= num1 && Deck2.Count >= num2)
			{
				var subgame = new Game { Deck1 = new Queue<int>(Deck1.Take(num1)), Deck2 = new Queue<int>(Deck2.Take(num2)) };
				winner = subgame.Play();
			}
			else
			{
				winner = num1 > num2 ? 1 : 2;
			}
			if (winner == 1)
			{
				Deck1.Enqueue(num1);
				Deck1.Enqueue(num2);
			}
			else
			{
				Deck2.Enqueue(num2);
				Deck2.Enqueue(num1);
			}
		}

		return Deck1.Count > 0 ? 1 : 2;
	}

	public long GetSum(int winner)
	{
		var winningDeck = winner == 1 ? Deck1 : Deck2;
		var sum = 0L;
		while (winningDeck.Count > 0)
		{
			var num = winningDeck.Dequeue();
			sum += num * (winningDeck.Count + 1);
		}
		return sum;
	}

	public override string ToString()
	{
		return base.ToString();
	}
}

var game = Game.CreateGameFromStdin();
var winner = game.Play();
var sum = game.GetSum(winner);
Console.WriteLine($"winner = {winner}, sum = {sum}");