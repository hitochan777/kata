class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        dp = [[1000000] * (len(dungeon[0])+1) for _ in range(len(dungeon)+1)]
        dp[len(dungeon)][len(dungeon[0])-1] = 0
        dp[len(dungeon)-1][len(dungeon[0])] = 0
        print(dp)
        
        for i in range(len(dungeon)-1, -1, -1):
            for j in range(len(dungeon[0])-1, -1, -1):
                dp[i][j] = max(0, -dungeon[i][j] + min(dp[i+1][j], dp[i][j+1]))
                
        return max(0, dp[0][0]) + 1
