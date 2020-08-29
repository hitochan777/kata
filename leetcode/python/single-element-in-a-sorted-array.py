from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, h = 0, len(nums)
        while l <= h:
            if l + 1 == h:
                return nums[l]
            m = (l + h) // 2
            if m + 1 < len(nums) and nums[m + 1] == nums[m]:
                if (len(nums) - m) % 2 == 0:
                    h = m - 1
                else:
                    l = m + 1
            elif m - 1 >= 0 and nums[m-1] == nums[m]:
                if m % 2 == 0:
                    h = m - 1
                else:
                    l = m + 1
            else:
                return nums[m]

        return None


if __name__ == "__main__":
    solver = Solution()
    actual = solver.singleNonDuplicate([1,1,2,2,4,4,5,5,9])
    assert actual == 9, actual
    actual = solver.singleNonDuplicate([1,1,2,3,3,4,4,8,8])
    assert actual == 2, actual
    actual = solver.singleNonDuplicate([3,3,7,7,10,11,11])
    assert actual == 10, actual
    actual = solver.singleNonDuplicate([3,3,7])
    assert actual == 7, actual
    actual = solver.singleNonDuplicate([7])
    assert actual == 7, actual
    actual = solver.singleNonDuplicate([2,3,3])
    assert actual == 2, actual
