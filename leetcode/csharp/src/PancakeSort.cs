using System.Collections.Generic;
using System.Linq;

namespace src
{
	public class PancakeSort
	{
		private IList<int> Flip(IList<int> A, int index)
		{
			int n = A.Count;
			var flippedList = A.Take(index + 1).Reverse().ToList();
			flippedList.AddRange(A.TakeLast(n - index - 1));
			return flippedList;
		}

		private void FlipAndLog(IList<int> A, int index, IList<int> flips)
		{
			Flip(A, index + 1);
			flips.Add(index + 1);
		}

		public IList<int> Solve(int[] A)
		{
			var flips = new List<int>();
			int n = A.Length;
			int cnt = 0; // number of sorted elements
			while (cnt < A.Length)
			{
				var subarray = A.Take(n - cnt).ToList();
				int max = subarray.Max();
				int index = subarray.ToList().FindIndex(val => val == max);
				FlipAndLog(A, index, flips);
				FlipAndLog(A, n - cnt - 1, flips);

				cnt++;
			}

			return flips;
		}
	}
}
