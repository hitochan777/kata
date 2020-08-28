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
					map.Add(interval[0], i);
				}
			}

			int[] keys = map.Keys.ToArray();
			return intervals.Select(interval =>
			{
				var lowerBound = GetLowerBound(keys, interval[1]);
				if (lowerBound >= 0)
				{
					return map[keys[lowerBound]];
				}

				return -1;
			}).ToArray();
		}

		public int GetLowerBound(int[] array, int value)
		{
			int low = 0, high = array.Length - 1;
			while (low <= high)
			{
				int mid = (low + high) >> 1;
				if (array[mid] == value)
				{
					while (mid + 1 < array.Length && array[mid + 1] == value)
					{
						mid++;
					}

					return mid;
				}
				else if (array[mid] < value)
				{
					low = mid + 1;
				}
				else
				{
					high = mid - 1;
				}
			}

			if (low >= array.Length)
			{
				return -1;
			}

			return low;
		}
	}
}
