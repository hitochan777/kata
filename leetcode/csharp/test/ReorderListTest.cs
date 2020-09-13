using System.Collections.Generic;
using NUnit.Framework;
using src;

namespace test
{
	public class ReorderListTest
	{
		private static ListNode GenerateLinkedListFromValues(List<int> values)
		{
			var dummyHead = new ListNode(0, null);
			var p = dummyHead;
			foreach (var value in values)
			{
				p.next = new ListNode(value, null);
				p = p.next;
			}

			return dummyHead.next;
		}

		private static List<int> ConvertToList(ListNode head)
		{
			var list = new List<int>();
			var p = head;
			while (p != null)
			{
				list.Add(p.val);
				p = p.next;
			}

			return list;
		}

		[Test]
		public void TestOddNumberOfElements()
		{
			var expected = new List<int> { 1, 5, 2, 4, 3 };
			var solver = new ListReorderer();
			var linkedList = GenerateLinkedListFromValues(new List<int> { 1, 2, 3, 4, 5 });
			solver.ReorderList(linkedList);
			var actual = ConvertToList(linkedList);
			Assert.AreEqual(actual, expected);
		}

		[Test]
		public void TestEvenNumberOfElements()
		{
			var expected = new List<int> { 1, 4, 2, 3 };
			var solver = new ListReorderer();
			var linkedList = GenerateLinkedListFromValues(new List<int> { 1, 2, 3, 4 });
			solver.ReorderList(linkedList);
			var actual = ConvertToList(linkedList);
			Assert.AreEqual(actual, expected);
		}

		[Test]
		public void TestEmptyList()
		{
			var expected = new List<int> { };
			var solver = new ListReorderer();
			var linkedList = GenerateLinkedListFromValues(new List<int> { });
			solver.ReorderList(linkedList);
			var actual = ConvertToList(linkedList);
			Assert.AreEqual(actual, expected);
		}

		[Test]
		public void TestOneElement()
		{
			var expected = new List<int> { 1 };
			var solver = new ListReorderer();
			var linkedList = GenerateLinkedListFromValues(new List<int> { 1 });
			solver.ReorderList(linkedList);
			var actual = ConvertToList(linkedList);
			Assert.AreEqual(actual, expected);
		}
	}
}
