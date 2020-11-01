namespace src
{
	public class ConvertBinaryNumberInLinkedListToInteger
	{
		public int GetDecimalValue(ListNode head)
		{
			var val = 0;
			while (head != null)
			{
				val = head.val + (val << 1);
				head = head.next;
			}
			return val;
		}
	}
}
