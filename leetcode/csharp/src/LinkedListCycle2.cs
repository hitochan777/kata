namespace src
{
	class LinkedListCycle2
	{
		public ListNode DetectCycle(ListNode head)
		{
			ListNode walker = head;
			ListNode runner = head;
			while (runner?.next != null)
			{
				runner = runner.next.next;
				walker = walker.next;
				if (runner == walker)
				{
					ListNode seeker = head;
					while (seeker != walker)
					{
						seeker = seeker.next;
						walker = walker.next;
					}
					return walker;
				}
			}
			return null;
		}
	}
}
