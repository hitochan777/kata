from typing import List
from collections import Counter

class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    cnts = Counter(nums)
    for num, freq in cnts.items():
      if freq > len(nums) // 2:
        return num
