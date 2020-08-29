from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rn_cnt = Counter(ransomNote)
        mg_cnt = Counter(magazine)
        for c, freq in rn_cnt.items():
            if c not in mg_cnt or freq > mg_cnt[c]:
                return False

        return True

if __name__ == "__main__":
    solver = Solution()
    assert not solver.canConstruct("a", "b")
    assert not solver.canConstruct("aa", "ab")
    assert solver.canConstruct("aa", "aab")
         
