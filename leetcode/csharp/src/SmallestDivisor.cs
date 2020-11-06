using System.Linq;
using System;

public class SmallestDivisor {
    public int Solve(int[] nums, int threshold) {
			var low = nums.Min()
			var high = nums.Max()
			// var mid = (low + high) >> 1;
			for (var i = high; i >= low; i--)
			{
				nums.Select( num => Math.Ceiling((decimal)num / i)).Sum()
			}
    }
}
