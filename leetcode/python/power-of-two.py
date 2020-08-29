class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n == 1 or Counter(bin(n))["1"] == 1)
