using System;
using System.Linq;

namespace src
{
	public class GoatLatin
	{
		public string ToGoatLatin(string s)
		{
			s.Split(new char[] {' '}).Select(
				word =>
				{
					char c = word[0];
					if (!(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'))
					{
					}
				}
			);
		}
	}
}
