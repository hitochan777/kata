class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        partial_subsets = self.subsets(nums[1:])
        return [[nums[0]] + partial for partial in partial_subsets] + partial_subsets
