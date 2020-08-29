public class Solution {
	public int ArrangeCoins(int n) {
		return ((int)Math.Sqrt(1L + 8L * (long)n) - 1) / 2;
	}
}
