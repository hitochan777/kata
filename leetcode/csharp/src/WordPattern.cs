using System;
using Sysmte.Collection.Generics;

namespace src
{
	public class WordPattern
	{
		public bool Solve(string pattern, string str)
		{
			var map = new Dictionary<char, string>();
			var invMap = new Dictionary<string, char>();
			string[] words = str.Split();
			if (pattern.Length != words.Length)
			{
				return false;
			}
			for (int i = 0; i < words.Length; i++)
			{
				char ch = pattern[i];
				if (map.ContainsKey(ch))
				{
					if (map[ch] != words[i])
					{
						return false;
					}
				}
				if (invMap.ContainsKey(words[i]))
				{
					if (invMap[words[i]] != map[ch])
					{
						return false;
					}
				}
				map[ch] = words[i];
			}
			return true;
		}
	}
}
