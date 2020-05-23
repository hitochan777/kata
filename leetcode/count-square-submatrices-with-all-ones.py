class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ans = 0
        n, m = len(matrix), len(matrix[0])
        dp = [[0] * m, [0] * m]
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    dp[i%2][j] = 0
                    continue
                    
                dp[i%2][j] = 1
                if j > 0:
                    dp[i%2][j] += min(dp[(i-1)%2][j], dp[(i-1)%2][j-1], dp[i%2][j-1])
                    
                ans += dp[i%2][j]
                
        return ans
