using System.Linq;
using System;

namespace SmallestDivisor
{
	public class SmallestDivisor
	{
		public int Solve(int[] nums, int threshold)
		{
			var low = 1;
			var high = nums.Max();
			var mid = (low + high) >> 1;
			var ans = mid;
			while (low <= high)
			{
				var sum = nums.Select(num => Math.Ceiling((decimal)num / mid)).Sum();
				if (sum <= threshold)
				{
					high = mid - 1;
					ans = mid;
				}
				else
				{
					low = mid + 1;
				}
				mid = (low + high) >> 1;
			}
			return ans;
		}

		public static void Main(string[] args)
		{
			var solver = new SmallestDivisor();
			Console.WriteLine(solver.Solve(new[] { 1, 2, 5, 9 }, 6));
			Console.WriteLine(solver.Solve(new[] { 2, 3, 5, 7, 11 }, 11));
			Console.WriteLine(solver.Solve(new[] { 19 }, 5));
		}
	}
}
