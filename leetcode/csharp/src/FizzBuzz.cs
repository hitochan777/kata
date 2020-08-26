using System.Collections.Generic;
using System.Linq;

namespace src
{
	public class FizzBuzz
	{
		private string GetOneFizzBuzz(int n)
		{
			if (n % 15 == 0)
			{
				return "FizzBuzz";
			}

			if (n % 3 == 0)
			{
				return "Fizz";
			}

			if (n % 5 == 0)
			{
				return "Buzz";
			}

			return $"{n}";
		}

		public IList<string> Solve(int n)
		{
			return Enumerable.Range(1, n).Select(GetOneFizzBuzz).ToList();
		}
	}
}
