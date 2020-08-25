using System.Collections.Generic;
using NUnit.Framework;
using src;

namespace test
{
	public class MincostTicketsTest
	{
		[Test]
		public void Test1()
		{
			var days = new int[] {1, 4, 6, 7, 8, 20};
			var costs = new int[] {2, 7, 15};
			int expected = 11;
			var solver = new MincostTickets();
			var actual = solver.Solve(days, costs);
			Assert.AreEqual(expected, actual);
		}

		[Test]
		public void Test2()
		{
			var days = new int[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31};
			var costs = new int[] {2, 7, 15};
			int expected = 17;
			var solver = new MincostTickets();
			var actual = solver.Solve(days, costs);
			Assert.AreEqual(expected, actual);
		}

		[Test]
		public void Test3()
		{
			var days = new int[] {1, 4, 6, 7, 8, 20};
			var costs = new int[] {2, 7, 15};
			int expected = 11;
			var solver = new MincostTickets();
			var actual = solver.Solve(days, costs);
			Assert.AreEqual(expected, actual);
		}

		[Test]
		public void Test4()
		{
			var days = new int[] {1, 4, 6, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 23, 27, 28};
			var costs = new int[] {3, 13, 45};
			int expected = 44;
			var solver = new MincostTickets();
			var actual = solver.Solve(days, costs);
			Assert.AreEqual(expected, actual);
		}

		[Test]
		public void Test5()
		{
			var days = new int[] {1,2,3,4,6,8,9,10,13,14,16,17,19,21,24,26,27,28,29};
			var costs = new int[] {3, 14, 50};
			int expected = 50;
			var solver = new MincostTickets();
			var actual = solver.Solve(days, costs);
			Assert.AreEqual(expected, actual);
		}
	}
}
