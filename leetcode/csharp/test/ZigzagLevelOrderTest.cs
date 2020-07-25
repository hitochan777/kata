using System.Collections.Generic;
using NUnit.Framework;

namespace ZigzagLevelOrder
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
            var root = new TreeNode { val = 3, left = new TreeNode { val = 9 }, right = new TreeNode { val = 20, left = new TreeNode { val = 15 }, right = new TreeNode { val = 7 } } };
            Assert.AreEqual(solver.ZigzagLevelOrder(root), new List<List<int>> { new List<int> { 3 }, new List<int> { 20, 9 }, new List<int> { 15, 7 } });
        }

        [Test]
        public void Test2()
        {
            var solver = new Solution();
            TreeNode root = null;
            Assert.AreEqual(solver.ZigzagLevelOrder(root), new List<List<int>> {});
        }

    }
}
