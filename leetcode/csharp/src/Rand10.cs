using System;

namespace src
{
	public class Rand10
	{
		private int Rand7()
		{
			var random = new Random();
			return random.Next(1, 7);
		}

		public int Solve()
		{
			int val;
			do
			{
				val = (Rand7() - 1) * 7 + Rand7();
			} while (val >= 41);

			return val % 10 + 1;
		}
	}
}
