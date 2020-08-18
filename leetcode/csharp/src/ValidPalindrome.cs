using System;
using System.Linq;

namespace IsPalindrome
{
	public class Solution
	{
		public bool IsPalindrome(string s)
		{
			s = new string(s.ToLower().Where(c => { return (c >= '0' && c <= '9') || (c >= 'a' && c <= 'z'); })
				.ToArray());
			for (int i = 0; i < s.Length / 2; i++)
			{
				if (s[i] != s[s.Length - i - 1])
				{
					return false;
				}
			}

			return true;
		}
	}

	public class Program
	{
		public static void Main()
		{
			var solver = new Solution();
			Console.WriteLine(solver.IsPalindrome("A man, a plan, a canal: Panama"));
			Console.WriteLine(solver.IsPalindrome("race a car"));
		}
	}

}
