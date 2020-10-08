namespace src
{
	public class RotateRight
	{
		public ListNode Solve(ListNode head, int k)
		{
			if (head == null || k == 0)
			{
				return head;
			}
			var n = 0;
			var p = head;
			var tail = p;
			while (p != null)
			{
				n++;
				tail = p;
				p = p.next;
			}
			var shift = n - (k % n);
			if (shift == n)
			{
				return head;
			}
			p = head;
			ListNode prev = null;
			while (shift > 0)
			{
				prev = p;
				p = p.next;
				shift--;
			}
			prev.next = null;
			var newHead = p;
			tail.next = head;
			return newHead;
		}
	}
}
