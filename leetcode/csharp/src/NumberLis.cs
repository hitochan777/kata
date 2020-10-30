using System.Linq;

public class Solution {
    public int FindNumberOfLIS(int[] nums) {
        var n = nums.Length;
        var dp = new int[n];
        for (int i = 0; i < n; i++)
        {
            for(int j = i + 1; j < n; j++)
            {
                if (nums[j] > nums[i] && dp[j] < dp[i] + 1)
                {
                    dp[j] = dp[i] + 1;
                }
            }
        }
        return dp.Max();
    }
}
