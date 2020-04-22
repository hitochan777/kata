from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        m = defaultdict(int)
        m[0] = 1
        s = 0
        count = 0
        for num in nums:
            s += num
            count += m[s - k]
            m[s] += 1

        return count


if __name__ == "__main__":
    solver = Solution()
    assert solver.subarraySum([1,1,1], 2) == 2
    assert solver.subarraySum([1], 0) == 0
