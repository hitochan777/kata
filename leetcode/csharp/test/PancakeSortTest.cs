using NUnit.Framework;
using System.Collections.Generic;
using System.Linq;
using src;

namespace test
{
	public static class ListExtension
	{
		public static List<T> ReverseUntil<T>(this List<T> list, int count)
		{
			return list.Take(count).Reverse().Concat(list.TakeLast(list.Count - count)).ToList();
		}

		public static bool IsSorted(this List<int> list)
		{
			for (int i = 1; i < list.Count; i++)
			{
				if (list[i - 1] > list[i])
				{
					return false;
				}
			}

			return true;
		}
	}

	public class PancakeSortTest
	{
		[Test]
		public void Test1()
		{
			var input = new List<int> { 3, 2, 4, 1 };
			var solver = new PancakeSort();
			var flips = solver.Solve(input.ToArray());
			foreach (int flip in flips)
			{
				input = input.ReverseUntil(flip);
			}

			Assert.True(input.IsSorted());
		}

		[Test]
		public void Test2()
		{
			var input = new List<int> { 1, 9, 8, 21, 2, 3, 5, 12, 3, 2 };
			var solver = new PancakeSort();
			var flips = solver.Solve(input.ToArray());
			foreach (int flip in flips)
			{
				input = input.ReverseUntil(flip);
			}

			Assert.True(input.IsSorted());
		}
	}
}
