using System.Collections.Generic;

namespace src
{
	public class CombinationSum3
	{
		public class Solution
		{
			private void CombinationSum3(IList<IList<int>> result, IList<int> cur, int k, int start, int sum)
			{
				if (sum < 0)
				{
					return;
				}

				if (sum == 0 && cur.Count == k)
				{
					result.Add(new List<int>(cur));
					return;
				}

				for (int i = start; i <= 9; i++)
				{
					cur.Add(i);
					CombinationSum3(result, cur, k, i + 1, sum - i);
					cur.RemoveAt(cur.Count - 1);
				}
			}

			public IList<IList<int>> CombinationSum3(int k, int n)
			{
				var result = new List<IList<int>>();
				var cur = new List<int>();
				CombinationSum3(result, cur, k, 1, n);
				return result;
			}
		}
	}
}
