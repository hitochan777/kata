using System;

namespace src
{
	public class ArrangingCoins
	{
		public int Solve(int n)
		{
			return ((int) Math.Sqrt(1L + 8L * (long) n) - 1) / 2;
		}
	}
}
