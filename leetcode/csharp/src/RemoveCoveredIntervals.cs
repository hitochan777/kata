namespace src
{
	public class RemoveCoveredIntervals
	{
		private bool isCovered(int[] interval1, int[] interval2)
		{
			if (interval2[0] <= interval1[0] && interval1[1] <= interval2[1])
			{
				return true;
			}
			return false;
		}

		public int Solve(int[][] intervals)
		{
			var cnt = 0;
			var n = intervals.Length;
			for (var i = 0; i < n; i++)
			{
				for (var j = 0; j < n; j++)
				{
					if (i == j)
					{
						continue;
					}
					if (isCovered(intervals[i], intervals[j]))
					{
						cnt++;
						break;
					}
				}
			}
			return n - cnt;
		}
	}
}
