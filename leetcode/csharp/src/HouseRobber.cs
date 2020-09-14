using System;
using System.Linq;
using NUnit.Framework;

namespace src
{
	public class HouseRobber
	{
		public int Rob(int[] nums)
		{
			var n = nums.Length;
			if (n == 0)
			{
				return 0;
			}
			if (n == 1)
			{
				return nums[0];
			}
			var dp = new int[n];
			dp[0] = nums[0];
			dp[1] = Math.Max(nums[0], nums[1]);
			for (var i = 2; i < n; i++)
			{
				dp[i] = Math.Max(nums[i] + dp[i - 2], dp[i - 1]);
			}
			return dp[n - 1];
		}
	}
}
