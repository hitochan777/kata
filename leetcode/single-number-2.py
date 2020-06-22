class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        high, low = 0, 0
        for num in nums:
            high, low = (high & ~low & ~num) | (~high & low & num), (~high & ~low & num) | (~high & low & ~num)

        return low

