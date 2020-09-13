using NUnit.Framework;

namespace WordSearch
{
	public class Tests
	{
		[SetUp]
		public void Setup()
		{
		}

		[Test]
		public void Test1()
		{
			var solver = new Solution();
			var board = new char[][]
			{
			  new char[] { 'A','B','C','E', },
			  new char[] { 'S','F','C','S' },
			  new char[] { 'A','D','E','E'}
			};
			Assert.IsTrue(solver.Exist(board, "ABCCED"));
			Assert.IsTrue(solver.Exist(board, "SEE"));
			Assert.IsFalse(solver.Exist(board, "ABCB"));
		}

		[Test]
		public void Test2()
		{
			var solver = new Solution();
			var board = new char[][]
			{
			  new char[] { 'a'},
			};
			Assert.IsTrue(solver.Exist(board, "a"));
		}

	}
}
