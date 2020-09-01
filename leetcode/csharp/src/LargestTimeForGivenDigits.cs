using System;
using System.Linq;
using System.Collections.Generic;

namespace src
{
	public class LargestTimeForGivenDigits
	{
		public List<List<int>> GetPermutations(int[] list)
		{
			if (list.Length == 0)
			{
				return new List<List<int>>();
			}

			if (list.Length == 1)
			{
				return new List<List<int>> {list.ToList()};
			}

			var permutations = new List<List<int>> { };
			var subPerms = GetPermutations(list.Skip(1).ToArray());
			foreach (var subPerm in subPerms)
			{
				for (int i = 0; i <= subPerm.Count; i++)
				{
					var latter = new List<int> {list[0]};
					latter.AddRange(subPerm.TakeLast(subPerm.Count - i));
					var newPerm = subPerm.Take(i).Concat(latter).ToList();
					permutations.Add(newPerm);
				}
			}

			return permutations;
		}

		public string Solve(int[] A)
		{
			string maxStr = "";
			var permutations = GetPermutations(A);
			foreach (var permutation in permutations)
			{
				if (permutation[0] >= 3)
				{
					continue;
				}

				if (permutation[0] == 2 && permutation[1] >= 4)
				{
					continue;
				}

				if (permutation[2] >= 6)
				{
					continue;
				}

				string newStr = $"{permutation[0]}{permutation[1]}:{permutation[2]}{permutation[3]}";
				if (String.Compare(newStr, maxStr) > 0)
				{
					maxStr = newStr;
				}
			}

			return maxStr;
		}
	}
}
