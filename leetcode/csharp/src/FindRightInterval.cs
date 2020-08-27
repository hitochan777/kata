using System;
using System.Collections.Generic;
using System.Linq;

namespace src
{
	public class FindRightInterval
	{
		public int[] Solve(int[][] intervals)
		{
			var map = new SortedDictionary<int, int>();
			for (int i = 0; i < intervals.Length; i++)
			{
				var interval = intervals[i];
				if (!map.ContainsKey(interval[0]))
				{
					map.Add(interval[0], i + 1);
				}
			}

			int[] keys = map.Keys.ToArray();
			return intervals.Select(interval => GetLowerBound(keys, interval[1])).ToArray();
		}

		public int GetLowerBound(int[] array, int value)
		{
			int low = 0, high = array.Length - 1;
			while (low <= high)
			{
				int mid = (low + high) >> 1;
				if (array[mid] <= value)
				{
					low = mid + 1;
				}
				else
				{
					high = mid;
				}
			}

			return low;
		}
	}
}
