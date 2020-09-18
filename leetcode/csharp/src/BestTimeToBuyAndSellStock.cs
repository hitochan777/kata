using System;

namespace src
{
	public class BestTimeToBuyAndSellStock
	{
		public int MaxProfit(int[] prices)
		{

			var maxval = 0;
			for (var i = 0; i < prices.Length; i++)
			{
				for (var j = i + 1; j < prices.Length; j++)
				{
					maxval = Math.Max(maxval, prices[j] - prices[i]);
				}
			}
			return maxval;
		}
	}
}
