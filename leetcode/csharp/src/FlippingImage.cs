using System.Linq;

namespace src {
	public class FlipImage {
		public int[][] Solve(int[][] A) {
			return A.Select(
					row => row.Reverse().Select( val => val == 0 ? 1 : 0).ToArray()
					).ToArray();
		}
	}
}

