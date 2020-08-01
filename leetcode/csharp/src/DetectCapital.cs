using System;
using System.Text.RegularExpressions;

public class Solution {
    public bool DetectCapitalUse(string word) {
        string pattern = @"^[A-Z]?([A-Z]+|[a-z]+)$";
		Regex regex = new Regex(pattern);
		return regex.IsMatch(word);
    }
}
					
public class Program
{
	public static void Main()
	{
		var solver = new Solution();
		Console.WriteLine(solver.DetectCapitalUse("USA"));
		Console.WriteLine(solver.DetectCapitalUse("Word"));
		Console.WriteLine(solver.DetectCapitalUse("word"));
		Console.WriteLine(solver.DetectCapitalUse("fLAG"));
	}
}
