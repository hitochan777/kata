from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0

        max_len = 0
        n, m = len(matrix), len(matrix[0])
        dp1 = [0] * (m + 1)
        for i in range(n):
            dp2 = [0] * (m + 1)
            for j in range(m):
                if matrix[i][j] == "0":
                    continue

                dp2[j+1] = min(dp1[j], dp1[j+1], dp2[j]) + 1

            dp1 = dp2
            max_len = max(max(dp1), max_len)

        return max_len * max_len


if __name__ == "__main__":
    solver = Solution()
    assert solver.maximalSquare(
        [
            ["1", "0", "1", "0", "0"], 
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ]
    ) == 4
    assert solver.maximalSquare([]) == 0
    assert solver.maximalSquare([["0"]]) == 0
