using System;
using System.Collections.Generic;

namespace src
{
	public class KDiffPairsInAnArray
	{
		public int FindPairs(int[] nums, int k)
		{
			var sum = 0;
			var counts = new Dictionary<int, int>();
			foreach (var num in nums)
			{
				if (counts.ContainsKey(num))
				{
					counts[num]++;
				}
				else
				{
					counts[num] = 1;
				}
			}

			foreach (var (num, count) in counts)
			{
				if (!counts.ContainsKey(num + k))
				{
					continue;
				}

				if (k == 0)
				{
					if (counts[num] > 1)
					{
						sum++;
					}
				}
				else
				{
					sum++;
				}
			}

			return sum;
		}
	}
}
