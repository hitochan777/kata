using NUnit.Framework;
using src;

namespace test
{
	public class FindRightIntervalTest
	{
		[Test]
		public void GetLowerBoundTest1()
		{
			var input = new int[] {1, 3, 6};
			var solver = new FindRightInterval();
			Assert.AreEqual(0, solver.GetLowerBound(input, 0));
			Assert.AreEqual(1, solver.GetLowerBound(input, 2));
			Assert.AreEqual(1, solver.GetLowerBound(input, 3));
			Assert.AreEqual(2, solver.GetLowerBound(input, 4));
			Assert.AreEqual(2, solver.GetLowerBound(input, 5));
			Assert.AreEqual(2, solver.GetLowerBound(input, 6));
			Assert.AreEqual(-1, solver.GetLowerBound(input, 7));
		}

		[Test]
		public void Test1()
		{
			var input = new int[][] {new int[] {3, 4}, new int[] {2, 3}, new int[] {1, 2}};
			var expected = new int[] {-1, 0, 1};
			var solver = new FindRightInterval();
			var actual = solver.Solve(input);
			Assert.AreEqual(expected, actual);
		}
	}
}
