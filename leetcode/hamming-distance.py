class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        cnts = Counter(bin(x ^ y))
        return cnts["1"]
