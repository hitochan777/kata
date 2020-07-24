using System.Collections.Generic;
using System.Linq;

namespace AllPathsFromSourceToTarget
{
    public class Solution
    {
        public List<IList<int>> findPaths(int[][] graph, int current, int target)
        {
            if (current == target)
            {
                return new List<IList<int>> { new List<int> { target } };
            }
            var paths = new List<IList<int>>();
            for (int i = 0; i < graph[current].Length; i++)
            {
                paths.AddRange(findPaths(graph, graph[current][i], target));
            }
            foreach (var path in paths)
            {
                path.Insert(0, current);
            }
            return paths;
        }
        public IList<IList<int>> AllPathsSourceTarget(int[][] graph)
        {

            return findPaths(graph, 0, graph.Length - 1);
        }
    }
}
