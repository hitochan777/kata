class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        
        nums.sort()
        prev = [-1] * n
        cnts = [0] * n
        max_idx, max_cnt = -1, 0
        for i in range(1, n):
            for j in range(0, i):
                if nums[i] % nums[j] == 0 and cnts[i] < cnts[j] + 1:
                    cnts[i] = cnts[j] + 1
                    prev[i] = j
                    
            if max_cnt < cnts[i]:
                max_cnt, max_idx = cnts[i], i
                    
        if max_idx == -1:
            return [nums[0]]
        
        result = []
        idx = max_idx
        while idx >= 0:
            result.append(nums[idx])
            idx = prev[idx]
        
        return result
