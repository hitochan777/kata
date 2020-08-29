class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, s, e = 0, 0, len(nums) - 1
        while i <= e:
            if nums[i] == 0:
                nums[s], nums[i] = nums[i], nums[s] 
                s += 1
                i += 1
            elif nums[i] == 2:
                nums[e], nums[i] = nums[i], nums[e]
                e -= 1
            else:
                i+=1
