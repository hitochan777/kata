using System.Collections.Generic;
using System.Linq;

namespace src
{
	public class PancakeSort
	{
		private List<int> Flip(List<int> A, int index)
		{
			int n = A.Count;
			int flipNum = index + 1;
			return A.Take(flipNum).Reverse().Concat(A.TakeLast(n - flipNum)).ToList();
		}

		private void FlipAndLog(List<int> A, int index, List<int> flips)
		{
			var flipped = Flip(A, index);
			A.Clear();
			A.AddRange(flipped);
			flips.Add(index + 1);
		}

		public IList<int> Solve(int[] A)
		{
			var list = A.ToList();
			var flips = new List<int>();
			int n = A.Length;
			int cnt = 0; // number of sorted elements
			while (cnt < A.Length - 1)
			{
				var subarray = list.Take(n - cnt).ToList();
				int max = subarray.Max();
				int index = subarray.ToList().FindIndex(val => val == max);
				FlipAndLog(list, index, flips);
				FlipAndLog(list, n - cnt - 1, flips);

				cnt++;
			}

			return flips;
		}
	}
}
