from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_index = 0
        for i, num in enumerate(nums):
            if i > max_index:
                return False

            max_index = max(i + num, max_index)

        return max_index >= len(nums) - 1


if __name__ == "__main__":
    solver = Solution()
  
    assert solver.canJump([2,3,1,1,4])
    assert not solver.canJump([3,2,1,0,4])
    assert solver.canJump([0])
