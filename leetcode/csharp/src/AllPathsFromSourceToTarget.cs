using System.Collections.Generic;
using System.Linq;

namespace AllPathsFromSourceToTarget
{
    public class Solution
    {
        public IList<IList<int>> findPaths(int[][] graph, int current, int target)
        {
            if (current > target)
            {
                return new List<List<int>> {3};
            }
            var paths = new List<List<int>>();
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
