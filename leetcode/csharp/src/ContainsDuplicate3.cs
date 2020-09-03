using System.Collections.Generic;

namespace src
{
	public class ContainsDuplicate3
	{
		public bool ContainsNearbyAlmostDuplicate(int[] nums, int k, int t)
		{
			int n = nums.Length;
			if (n <= 1 || t < 0 || k < 0)
			{
				return false;
			}

			var bucket = new Dictionary<int, int>();
			int width = t + 1;
			for (int i = 0; i < n; i++)
			{
				int bucketId = GetBucketId(nums[i], width);
				if (bucket.ContainsKey(bucketId))
				{
					return true;
				}

				if (bucket.ContainsKey(bucketId + 1) && bucket[bucketId + 1] - nums[i] < width)
				{
					return true;
				}

				if (bucket.ContainsKey(bucketId - 1) && nums[i] - bucket[bucketId - 1] < width)
				{
					return true;
				}

				bucket[bucketId] = nums[i];
				if (i >= k)
				{
					bucket.Remove(GetBucketId(nums[i - k], width));
				}
			}

			return false;
		}

		private int GetBucketId(int value, int width)
		{
			return value < 0 ? (value + 1) / width - 1 : value / width;
		}
	}
}
