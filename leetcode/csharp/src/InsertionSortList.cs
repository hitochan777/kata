namespace src
{
	public class InsertionSortList
	{
		public ListNode Solve(ListNode head)
		{
			var dummy = new ListNode();
			var cur = head;
			while (cur != null)
			{
				var curNext = cur.next;
				var prev = dummy;
				var next = dummy.next;
				while (next != null)
				{
					if (next.val > cur.val)
					{
						break;
					}
					prev = next;
					next = next.next;
				}
				cur.next = next;
				prev.next = cur;
				cur = curNext;
			}
			return dummy.next;
		}
	}
}
