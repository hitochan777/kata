class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        most_commons = Counter(nums).most_common(k)
        return list(map(lambda x: x[0], most_commons))
