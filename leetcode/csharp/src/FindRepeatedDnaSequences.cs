using System.Collections.Generic;
using System.Linq;

namespace src
{
	public class FindRepeatedDnaSequences
	{
		public IList<string> Solve(string s)
		{
			var counts = new Dictionary<string, int>();
			for (var i = 0; i < s.Length - 10; i++)
			{
				var str = s.Substring(i, 10);
				if (!counts.ContainsKey(str))
				{
					counts[str] = 0;
				}
				counts[str]++;
			}

			return counts.Where((str, cnt) => cnt > 1).Select(pair => pair.Key).ToList();
		}
	}
}
