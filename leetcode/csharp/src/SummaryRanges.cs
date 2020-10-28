using System.Collections.Generic;

namespace src
{
	public class SummaryRanges
	{
		private void AddSpan(int[] span, IList<string> list)
		{
			if (span[0] == span[1])
			{
				list.Add($"{span[0]}");
			}
			else
			{
				list.Add($"{span[0]}->{span[1]}");
			}
		}

		public IList<string> Solve(int[] nums)
		{
			if (nums.Length == 0)
			{
				return new List<string>();
			}
			var ans = new List<string>();
			var curSpan = new[] { nums[0], nums[0] };
			for (int i = 1; i < nums.Length; i++)
			{
				if (nums[i] == curSpan[1] + 1)
				{
					curSpan[1] = nums[i];
				}
				else
				{
					AddSpan(curSpan, ans);
					curSpan[0] = curSpan[1] = nums[i];
				}
			}
			AddSpan(curSpan, ans);
			return ans;
		}
	}
}
