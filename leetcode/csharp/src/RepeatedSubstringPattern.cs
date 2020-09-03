using System.Linq;

namespace src
{
	public class RepeatedSubstringPattern
	{
		public bool Solve(string s)
		{
			int n = s.Length;
			if (n <= 1)
			{
				return false;
			}

			for (int i = 1; i <= n >> 1; i++)
			{
				if (n % i != 0)
				{
					continue;
				}

				string repeated = string.Concat(Enumerable.Repeat(string.Concat(s.Take(i)), n / i));
				if (repeated == s)
				{
					return true;
				}
			}

			return false;
		}
	}
}
