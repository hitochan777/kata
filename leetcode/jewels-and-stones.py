from collections import Counter


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        counts = Counter(S)
        return sum(freq for c, freq in counts.items() if c in J)


if __name__ == "__main__":
    solver = Solution()
    assert solver.numJewelsInStones("aA", "aAAbbbb") == 3
    assert solver.numJewelsInStones("z", "ZZ") == 0
