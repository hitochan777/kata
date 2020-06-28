class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n+1)
        root = int(math.sqrt(n))
        for i in range(1, n+1):
            for j in range(1, root+1):
                if i == j**2:
                    dp[i] = 1
                elif i > j**2:
                    dp[i] = min(dp[i], dp[i - j**2] + 1)
                    
        return dp[n]
