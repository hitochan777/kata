using System.Linq;
using System.Collections.Generic;

namespace src
{
	public class NumbersWithSameConsecutiveDifferences
	{
		private int getLastDigit(int num)
		{
			return num % 10;
		}

		private void TryAdd(int partialNum, int modifiedLastDigit, List<int> nums)
		{
			if (modifiedLastDigit >= 0 && modifiedLastDigit <= 9)
			{
				nums.Add(int.Parse(partialNum.ToString() + modifiedLastDigit.ToString()));
			}
		}

		public int[] NumsSameConsecDiff(int N, int K)
		{
			if (N == 1)
			{
				return new int[] { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
			}

			var nums = new List<int>();
			var partialNums = NumsSameConsecDiff(N - 1, K);
			foreach (int partialNum in partialNums)
			{
				int lastDigit = getLastDigit(partialNum);
				TryAdd(partialNum, lastDigit + K, nums);
				TryAdd(partialNum, lastDigit - K, nums);
			}
			return nums.Where(num => num.ToString().Length == N).Distinct().ToArray();
		}
	}
}
