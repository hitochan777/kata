class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        prev, cur = num / 2, None
        while True:
            cur = prev - (prev ** 2 - num) / (2 * prev)

            if abs(cur - prev) < 1e-10:
                break

            prev = cur

        return int(cur) ** 2 == num


if __name__ == "__main__":
    solver = Solution()
    assert solver.isPerfectSquare(16)
    assert not solver.isPerfectSquare(14)
