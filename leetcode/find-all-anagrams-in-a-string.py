from typing import List
from collections import Counter, defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        indices = []
        pc = Counter(p)
        sc = Counter(s[0:len(p)])
        if pc == sc:
            indices.append(0)

        for i in range(1, len(s) - len(p) + 1):
            sc[s[i-1]] -= 1
            if sc[s[i-1]] == 0:
                del sc[s[i-1]]

            c = s[i + len(p) - 1]
            if c not in sc:
                sc[c] = 0

            sc[c] += 1
            if pc == sc:
                indices.append(i)

        return indices

if __name__ == "__main__":
    solver = Solution()
    assert solver.findAnagrams("cbaebabacd", "abc") == [0, 6]
    assert solver.findAnagrams("abab", "ab") == [0, 1, 2]
    assert solver.findAnagrams("baa", "aa") == [1]
