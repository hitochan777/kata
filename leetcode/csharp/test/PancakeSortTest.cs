using NUnit.Framework;
using System.Collections.Generic;
using System.Linq;
using src;

namespace test
{
	public class PancakeSortTest
	{
		private static bool IsSorted(int[] arr)
		{
			for (int i = 1; i < arr.Length; i++)
			{
				if (arr[i - 1] > arr[i])
				{
					return false;
				}
			}
			return true;
		}

		[Test]
		public void Test1()
		{
			var input = new List<int>{3, 2, 4, 1};
			var solver = new PancakeSort();
			var flips= solver.Solve(input.ToArray());
			foreach (int flip in flips)
			{
				input = input.Take(flip).Reverse().Concat(input.TakeLast(input.Count - flip)).ToList();
			}
			Assert.True(IsSorted(input.ToArray()));
		}
	}
}
