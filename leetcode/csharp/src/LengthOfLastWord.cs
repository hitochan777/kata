using System.Linq;

namespace src
{
	public class LengthOfLastWord
	{
		public int Solve(string s)
		{
			var lastWord = s.Trim().Split(new char[] { ' ' }).LastOrDefault();
			return lastWord == null ? 0 : lastWord.Length;
		}
	}
}
