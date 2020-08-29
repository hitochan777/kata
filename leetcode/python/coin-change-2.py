from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [ [0] * (len(coins) + 1) for _ in range(amount + 1)]
        for i in range(len(coins) + 1):
            dp[0][i] = 1

        for i in range(1, amount + 1):
            dp[i][0] = 0

        for i in range(1, amount + 1):
            for j in range(1, len(coins) + 1):
                val = coins[j-1]
                dp[i][j] = (dp[i - val][j] if i >= val else 0) + dp[i][j-1]

        return dp[-1][-1]

if __name__ == "__main__":
    solver = Solution()
    print(solver.change(5, [1,2, 5]))

