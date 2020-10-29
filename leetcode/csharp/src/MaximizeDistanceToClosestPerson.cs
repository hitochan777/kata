using System.Linq;
namespace src
{
	public class Solution
	{
		public int MaxDistToClosest(int[] seats)
		{
			var maxDiff = 0;
			var seatedIndices = seats.Select((seat, i) => new { seat, index = i }).Where(val => val.seat == 1).Select(val => val.index).ToArray();

			maxDiff = seatedIndices.First();
			var diff = seats.Length - 1 - seatedIndices.Last();
			if (diff > maxDiff)
			{
				maxDiff = diff;
			}
			for (int i = 1; i < seatedIndices.Length; i++)
			{
				diff = seatedIndices[i] - seatedIndices[i - 1];
				if (diff > maxDiff)
				{
					maxDiff = diff / 2;
				}
			}
			return maxDiff;
		}
	}
}
