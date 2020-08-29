from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) < 2:
            return False

        x, coef, b = None, None, None
        first, second = coordinates[0], coordinates[1]

        if abs(first[0] - second[0]) < 1e-10:
            x = first[0]
        else:
            coef = (first[1] - second[1]) / (first[0] - second[0])  # edge
            b = first[1] - coef * first[0] 

        if x is None:
            return all(abs(coef * c[0] + b - c[1]) < 1e-10 for c in coordinates[2:])

        return all(abs(c[0] - x) < 1e-10 for c in coordinates[2:])

def asserts(actual, expected):
    assert actual == expected, f"{actual=} {expected=}"

if __name__ == "__main__":
    solver = Solution()
    asserts(solver.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]), True)
    asserts(solver.checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]), False)
