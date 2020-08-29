namespace src
{
	public class RemoveLinkedListElements
	{
		public ListNode Solve(ListNode head, int val)
		{
			var prev = new ListNode(0, head);
			var root = prev;
			var p = head;
			while (p != null)
			{
				if (p.val == val)
				{
					prev.next = p.next;
				}
				else
				{
					prev = p;
				}

				p = p.next;
			}

			return root.next;
		}
	}
}
