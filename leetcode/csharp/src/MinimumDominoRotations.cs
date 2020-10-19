using System;
using System.Linq;
using System.Collections.Generic;

namespace MinDominoRotations
{
	public class Solution
	{
		public int MinDominoRotations(int[] A, int[] B)
		{
			var n = A.Length;
			var counts = new Dictionary<int, int>();
			foreach (var val in A.Concat(B))
			{
				if (!counts.ContainsKey(val))
				{
					counts[val] = 0;
				}
				counts[val]++;
			}
			var mostCommon = counts.Select(item => (value: item.Value, key: item.Key)).Max().key;
			var aCnt = 0;
			var bCnt = 0;
			for (int i = 0; i < n; i++)
			{
				if (A[i] == B[i])
				{
					if (A[i] == mostCommon)
					{
						continue;
					}
					else
					{
						return -1;
					}
				}
				else if (A[i] == mostCommon)
				{
					bCnt++;
				}
				else if (B[i] == mostCommon)
				{
					aCnt++;
				}
				else
				{
					return -1;
				}
			}
			return Math.Min(aCnt, bCnt);
		}
	}
}
