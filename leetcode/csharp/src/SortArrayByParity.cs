using System;
using System.Collections;

namespace src
{
	public class ParityComparer : IComparer
	{
		public int Compare(Object x, Object y)
		{
			return (int)x % 2 - (int)y % 2;
		}
	}

	public class SortArrayByParity
	{
		public int[] Solve(int[] A)
		{
			Array.Sort(A, new ParityComparer());
			return A;
		}
	}
}
