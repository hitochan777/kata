class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        cnt = 0
        if not grid:
            return 0
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    continue

                if i == 0 or grid[i-1][j] == 0:
                    cnt += 1

                if i == n - 1 or grid[i+1][j] == 0:
                    cnt += 1
                
                if j == 0 or grid[i][j-1] == 0:
                    cnt += 1

                if j == m - 1 or grid[i][j+1] == 0:
                    cnt += 1

        return cnt