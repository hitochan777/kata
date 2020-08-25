using System;
using System.Linq;

namespace src
{
	public class MincostTickets
	{
		public int Solve(int[] days, int[] costs)
		{
			int n = days.Length;
			int[] dp = new int[n+1];
			for (int i = 0; i < n+1; i++)
			{
				dp[i] = costs.Max() * n;
			}

			dp[0] = 0;

			for (int i = 1; i < n+1; i++)
			{
				dp[i] = Math.Min(dp[i - 1] + costs[0], dp[i]);
				for (int j = Math.Max(i - 7, 0); j < i; j++)
				{
					if (days[i - 1] - days[j] <= 6)
					{
						dp[i] = Math.Min(dp[j] + costs[1], dp[i]);
					}
				}

				for (int j = Math.Max(i - 30, 0); j < i; j++)
				{
					if (days[i - 1] - days[j] <= 29)
					{
						dp[i] = Math.Min(dp[j] + costs[2], dp[i]);
					}
				}
			}

			return dp[n];
		}
	}
}

