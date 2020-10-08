using System;

namespace src
{
	public class BinarySearch
	{
		public int Search(int[] nums, int target)
		{
			var index = Array.BinarySearch(nums, target);
			return index >= 0 ? index : -1;
		}
	}
}
