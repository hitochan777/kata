using System;

namespace BestTimeToBuyAndSellStock3
{
	public class Solution
	{
		public int MaxProfit(int[] prices)
		{
			int n = prices.Length;
			if (n < 2)
			{
				return 0;
			}

			var left = new int[n];
			var right = new int[n];
			int min = prices[0];
			for (int i = 1; i < n; i++)
			{
				min = Math.Min(prices[i], min);
				left[i] = Math.Max(left[i - 1], prices[i] - min);
			}

			int max = prices[n - 1];
			for (int i = n - 2; i >= 0; i--)
			{
				max = Math.Max(prices[i], max);
				right[i] = Math.Max(right[i + 1], max - prices[i]);
			}

			int ans = 0;
			for (int i = 0; i < n; i++)
			{
				ans = Math.Max(ans, left[i] + right[i]);
			}

			return ans;
		}
	}
}
