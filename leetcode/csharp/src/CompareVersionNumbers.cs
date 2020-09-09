using System;
using System.Linq;

namespace src
{
	public class CompareVersionNumbers
	{
		public int Solve(string version1, string version2)
		{
			var nums1 = version1.Split(".").Select(num => int.Parse(num)).ToArray();
			var nums2 = version2.Split(".").Select(num => int.Parse(num)).ToArray();
			for (int i = 0; i < Math.Max(nums1.Length, nums2.Length); i++)
			{
				int num1 = i < nums1.Length ? nums1[i] : 0;
				int num2 = i < nums2.Length ? nums2[i] : 0;
				if (num1 < num2)
				{
					return -1;
				}

				if (num1 > num2)
				{
					return 1;
				}
			}

			return 0;
		}
	}
}
