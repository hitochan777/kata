from typing import List
from collections import defaultdict

class Solution:
    def findJudge(self, N: int, trusts: List[List[int]]) -> int:
        if N == 1 and len(trusts) == 0:
            return 1

        cnts = defaultdict(int)
        trusting = defaultdict(bool)
        for trust in trusts:
            cnts[trust[1]] += 1
            trusting[trust[0]] = True

        candidates = [person for (person, cnt) in cnts.items() if cnt == N - 1]
        if len(candidates) != 1:
            return -1

        if trusting[candidates[0]]:
            return -1

        return candidates[0]




if __name__ == "__main__":
    solver = Solution()
    assert solver.findJudge(1, []) == 1
    assert solver.findJudge(2, [[1,2]]) == 2
    assert solver.findJudge(3, [[1,3],[2,3]]) == 3
    assert solver.findJudge(3, [[1,3],[2,3],[3,1]]) == -1
    assert solver.findJudge(3, [[1,2],[2,3]]) == -1
    assert solver.findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]) == 3
