using System.Linq;
namespace src
{
	public class Solution
	{
		public int MaxDistToClosest(int[] seats)
		{
			var maxDiff = 0;
			var index = 0;
			var seatedIndices = seats.Where(seat => seat == 1).Select((seat, i) => i).ToList();
			for (int i = 1; i < seatedIndices.Count; i++)
			{
				var diff = seatedIndices[i] - seatedIndices[i - 1];
				if (diff > maxDiff)
				{
					index = diff / 2 + seatedIndices[i - 1];
				}
			}
			return index;
		}
	}
}
