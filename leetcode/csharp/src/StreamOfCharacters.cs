using System.Collections.Generic;
using System.Linq;

namespace src
{
	public class Trie
	{
		public struct Letter
		{
			public const string Chars = "abcdefghijklmnopqrstuvwxyz";

			public static implicit operator Letter(char c)
			{
				return new Letter() { Index = Chars.IndexOf(c) };
			}

			public int Index;

			public char ToChar()
			{
				return Chars[Index];
			}

			public override string ToString()
			{
				return Chars[Index].ToString();
			}
		}

		public class Node
		{
			public string Word;

			public bool IsTerminal
			{
				get { return Word != null; }
			}

			public Dictionary<Letter, Node> Edges = new Dictionary<Letter, Node>();
		}

		public Node Root = new Node();

		public Trie(string[] words)
		{
			for (int w = 0; w < words.Length; w++)
			{
				var word = words[w];
				var node = Root;
				for (int len = 1; len <= word.Length; len++)
				{
					var letter = word[len - 1];
					Node next;
					if (!node.Edges.TryGetValue(letter, out next))
					{
						next = new Node();
						if (len == word.Length)
						{
							next.Word = word;
						}

						node.Edges.Add(letter, next);
					}

					node = next;
				}
			}
		}

		public bool FindWord(string str)
		{
			var chars = str.ToCharArray();
			Node tempRoot = Root;
			int total = chars.Count() - 1;
			for (int i = 0; i < chars.Count(); i++)
			{
				if (tempRoot.Edges.Keys.Contains(chars[i]))
				{
					tempRoot = tempRoot.Edges[chars[i]];

					if (total == i)
					{
						if (tempRoot.IsTerminal == true)
						{
							return true;
						}
					}
				}
				else
				{
					return false;
				}
			}

			return false;
		}
	}

	public class StreamChecker
	{
		private readonly Trie _trie;

		public StreamChecker(string[] words)
		{
			this._trie = new Trie(words);
		}

		public bool Query(char letter)
		{
			return this._trie.FindWord("");
		}
	}
}
