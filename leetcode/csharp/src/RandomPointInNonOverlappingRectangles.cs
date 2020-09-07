using System;
using System.Linq;

namespace src
{
	public class RandomPointInNonOverlappingRectangles
	{
		private int[][] Rects;
		private int[] Areas;
		public RandomPointInNonOverlappingRectangles(int[][] rects)
		{
			this.Rects = rects;
			this.Areas = rects.Select(rect => Math.Abs(rect[0] - rect[2]) * Math.Abs(rect[1] - rect[3])).ToArray();
		}

		private int SampleIndex(int[] weights)
		{
			var random = new Random();
			double randomValue = (int)(random.NextDouble() * weights.Sum());
			int current = 0;
			for (int i = 0; i < weights.Length; i++)
			{
				int weight = weights[i];
				if (randomValue >= current && randomValue < current + weight)
				{
					return i;
				}
				current += weight;
			}

			return weights.Length - 1;
		}

		public int[] Pick()
		{
			var random = new Random();
			int index = SampleIndex(this.Areas);
			var rand1 = random.NextDouble();
			var rand2 = random.NextDouble();
			return new[] { 0 };
		}
	}
}
