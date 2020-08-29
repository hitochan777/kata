class Solution:
    def findComplement(self, num: int) -> int:
        return int(bin(num ^ 0xFFFFFFFF)[-(len(bin(num)) - 2):], 2)
