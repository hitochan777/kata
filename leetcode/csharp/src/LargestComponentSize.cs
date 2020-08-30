using System.Collections.Generic;
using System.Linq;

namespace src
{
	class DisjointUnionSets
	{
		int[] rank, parent;
		int n;

		public DisjointUnionSets(int n)
		{
			rank = new int[n];
			parent = new int[n];
			this.n = n;
			MakeSet();
		}

		public void MakeSet()
		{
			for (int i = 0; i < n; i++)
			{
				parent[i] = i;
			}
		}

		public int Find(int x)
		{
			if (parent[x] != x)
			{
				parent[x] = Find(parent[x]);
			}

			return parent[x];
		}

		public void Union(int x, int y)
		{
			int xRoot = Find(x), yRoot = Find(y);
			if (xRoot == yRoot)
			{
				return;
			}

			if (rank[xRoot] < rank[yRoot])
			{
				parent[xRoot] = yRoot;
			}
			else if (rank[yRoot] < rank[xRoot])
			{
				parent[yRoot] = xRoot;
			}
			else
			{
				parent[yRoot] = xRoot;
				rank[xRoot] = rank[xRoot] + 1;
			}
		}
	}

	public class LargestComponentSize
	{
		public int Solve(int[] A)
		{
			var disjointSet = new DisjointUnionSets(A.Max() + 1);
			foreach (int num in A)
			{
				for (int i = 2; i * i <= num; i++)
				{
					disjointSet.Union(num, i);
					disjointSet.Union(num, num / i);
				}
			}

			var counter = new Dictionary<int, int>();
			foreach (int num in A)
			{
				int root = disjointSet.Find(num);
				if (!counter.ContainsKey(root))
				{
					counter[root] = 0;
				}

				counter[root]++;
			}

			return counter.Values.Max();
		}
	}
}
