using NUnit.Framework;
using src;
using System.Collections.Generic;
using System.Linq;

namespace test
{
	public class NumbersWithSameConsecutiveDifferencesTest
	{
		[SetUp]
		public void Setup()
		{
		}

		[Test]
		public void Test1()
		{
			var solver = new NumbersWithSameConsecutiveDifferences();
			var actual = solver.NumsSameConsecDiff(3, 7).ToHashSet();
			var expected = new HashSet<int> { 181, 292, 707, 818, 929 };
			Assert.IsTrue(expected.SetEquals(actual));
		}

		[Test]
		public void Test2()
		{
			var solver = new NumbersWithSameConsecutiveDifferences();
			var actual = solver.NumsSameConsecDiff(2, 1).ToHashSet();
			var expected = new HashSet<int> { 10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98 };
			Assert.IsTrue(expected.SetEquals(actual));
		}

		[Test]
		public void Test3()
		{
			var solver = new NumbersWithSameConsecutiveDifferences();
			var actual = solver.NumsSameConsecDiff(2, 0).ToHashSet();
			var expected = new HashSet<int> { 11, 22, 33, 44, 55, 66, 77, 88, 99 };
			Assert.IsTrue(expected.SetEquals(actual));
		}
	}
}
