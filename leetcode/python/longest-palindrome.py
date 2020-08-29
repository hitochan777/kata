class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        return sum(freq // 2 * 2 for _, freq in cnt.items()) + (1 if any(freq % 2 == 1 for _, freq in cnt.items()) else 0)
