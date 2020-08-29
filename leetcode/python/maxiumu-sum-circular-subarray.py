from functools import reduce

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        cur_max, cur_min = 0, 0
        max_val, min_val = -1e10, 1e10
        for val in A:
            cur_max, cur_min = max(cur_max + val, val), min(cur_min + val, val)
            max_val, min_val = max(cur_max, max_val), min(cur_min, min_val)
        
        return max_val if sum(A) == min_val else max(max_val, sum(A) - min_val)
