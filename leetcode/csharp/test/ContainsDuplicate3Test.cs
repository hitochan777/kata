using NUnit.Framework;
using src;

namespace test
{
	public class ContainsDuplicate3Test
	{
		[Test]
		public void Test1()
		{
			var solver = new ContainsDuplicate3();
			Assert.True(solver.ContainsNearbyAlmostDuplicate(new int[] {1, 2, 3, 1}, 3, 0));
		}

		[Test]
		public void Test2()
		{
			var solver = new ContainsDuplicate3();
			Assert.True(solver.ContainsNearbyAlmostDuplicate(new int[] {1, 0, 1, 1}, 1, 2));
		}

		[Test]
		public void Test3()
		{
			var solver = new ContainsDuplicate3();
			Assert.False(solver.ContainsNearbyAlmostDuplicate(new int[] {1, 5, 9, 1, 5, 9}, 2, 3));
		}
	}
}
