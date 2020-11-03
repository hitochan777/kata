using System;

namespace src {
	public class ConsecutiveCharacters
	{
		public int MaxPower(string s)
		{
			var prev = '*';
			var count = 0;
			var maxCount = 0;
			foreach (var c in s)
			{
				if (prev == c)
				{
					count++;
				}
				else
				{
					maxCount = Math.Max(maxCount, count);
					count = 1;
					prev = c;
				}
			}
			return Math.Max(maxCount, count);
		}
	}
}
