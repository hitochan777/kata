using System;

namespace src
{
	public class ComplementOfBase10Integer.cs {
        public int BitwiseComplement(int N)
	{
		var n = Convert.ToString(N, 2).Length;
		return ~N & ((1 << n) - 1);
	}
}
}
