using System;
using System.Collections.Generic;

namespace src
{
	public class InsertInterval
	{
		public int[][] Solve(int[][] intervals, int[] newInterval)
		{
			var result = new List<int[]>();
			foreach (var interval in intervals)
			{
				if (interval[1] < newInterval[0])
				{
					result.Add(interval);
					continue;
				}
				if (interval[0] > newInterval[1])
				{
					result.Add(newInterval);
					newInterval = interval;
					continue;
				}
				newInterval = new int[]
					{Math.Min(interval[0], newInterval[0]), Math.Max(interval[1], newInterval[1])};
			}
			result.Add(newInterval);
			return result.ToArray();
		}
	}
}
