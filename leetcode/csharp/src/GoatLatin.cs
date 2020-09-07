using System;
using System.Linq;
using System.Text;

namespace src
{
	public class GoatLatin
	{
		public string ToGoatLatin(string s)
		{
			return string.Join(' ', s.Split(new char[] { ' ' }).Select(
				(word, i) =>
				{
					var sb = new StringBuilder();
					char c = word.ToLower()[0];
					if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
					{
						sb.Append(word);
					}
					else
					{
						sb.Append(word.Substring(1));
						sb.Append(word[0]);
					}

					sb.Append("ma");
					sb.Append(new String('a', i + 1));
					return sb.ToString();
				}
			));
		}
	}
}
