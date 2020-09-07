namespace src
{
	public class ListNode
	{
		public int val;
		public ListNode next;

		public ListNode(int val = 0, ListNode next = null)
		{
			this.val = val;
			this.next = next;
		}
	}

	public class ListReorderer
	{
		private ListNode reverseList(ListNode head)
		{
			if (head == null)
			{
				return null;
			}

			ListNode cur = head.next;
			ListNode pre = head;
			while (cur != null)
			{
				ListNode tmp = cur.next;
				cur.next = pre;
				pre = cur;
				cur = tmp;
			}
			head.next = null;

			return pre;
		}

		private ListNode breakListInMiddle(ListNode head)
		{
			if (head?.next == null)
			{
				return null;
			}

			ListNode slow = head, fast = head.next;
			while (fast?.next != null)
			{
				slow = slow.next;
				fast = fast.next.next;
			}

			ListNode secondHead = slow.next;
			slow.next = null;
			return secondHead;
		}

		private void mergedLists(ListNode first, ListNode second)
		{
			while (first != null && second != null)
			{
				ListNode tmp1 = first.next;
				ListNode tmp2 = second.next;
				first.next = second;
				second.next = tmp1;

				first = tmp1;
				second = tmp2;
			}
		}

		public void ReorderList(ListNode head)
		{
			ListNode latterHead = breakListInMiddle(head);
			ListNode reversedLatterHead = reverseList(latterHead);
			mergedLists(head, reversedLatterHead);
		}
	}
}
