from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if len(nums) == 0 or len(nums) == 1:
            return False

        for i in range(max(len(nums) - k, 1)):
            a = sorted(nums[i:i+k+1])
            if any(abs(v1 - v2) <= t for v1, v2 in zip(a, a[1:])):
                return True

        return False
