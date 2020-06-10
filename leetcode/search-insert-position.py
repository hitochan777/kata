from typing import List
import bisect


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)


if __name__ == "__main__":
    solver = Solution()
    assert solver.searchInsert([1,3,5,6], 5) == 2
    assert solver.searchInsert([1,3,5,6], 2) == 1
    assert solver.searchInsert([1,3,5,6], 7) == 4
    assert solver.searchInsert([1,3,5,6], 0) == 0
