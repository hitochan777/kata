using NUnit.Framework;

namespace SuperPow
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
			Assert.AreEqual(8, solver.SuperPow(2, new[] { 3 }));
			Assert.AreEqual(1024, solver.SuperPow(2, new[] { 1, 0 }));
		}
	}
}
