from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, h = 0, len(nums)
        while l < h:
            if l + 1 == h:
                return nums[l]

            m = (l + h) // 2
            if m + 1 < len(nums) and nums[m + 1] == nums[m]:
                if (len(nums) - m) % 2 == 0:
                    l = m + 1
                else:
                    h = m - 1
            elif m - 1 >= 0 and nums[m-1] == nums[m]:
                if m % 2 == 0:
                    l = m + 1
                else:
                    h = m - 1       
            else:
                return nums[m]

        return None


if __name__ == "__main__":
    solver = Solution()
    assert solver.singleNonDuplicate([1,1,2,3,3,4,4,8,8]) == 2
    assert solver.singleNonDuplicate([3,3,7,7,10,11,11]) == 10 
