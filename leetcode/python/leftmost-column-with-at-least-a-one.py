from typing import List

class BinaryMatrix(object):
    def __init__(self, matrix):
        self.matrix = matrix
        self.counter = 0

    def get(self, x: int, y: int) -> int:
        if self.counter >= 1000:
            raise RuntimeError("cannot call get >= 1000 times")

        self.counter += 1
        return self.matrix[x][y]

    def dimensions(self) -> List[int]:
        if len(self.matrix) == 0:
            return [0,0]

        return [len(self.matrix), len(self.matrix[0])]

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        n, m = binaryMatrix.dimensions()
        min_index = 10000
        for i in range(n):
            l, h = 0, m
            while l != h:
                mid = (l + h) >> 1
                val = binaryMatrix.get(i, mid)
                if val == 0:
                    l = mid + 1
                else:
                    h = mid

            min_index = min(min_index, l)

        if min_index >= m:
            return -1

        return min_index
                


if __name__ == "__main__":
    solver = Solution()
    binaryMatrix = BinaryMatrix([[0,0],[1,1]])
    assert solver.leftMostColumnWithOne(binaryMatrix) == 0

    binaryMatrix = BinaryMatrix([[0,0],[0,1]])
    assert solver.leftMostColumnWithOne(binaryMatrix) == 1

    binaryMatrix = BinaryMatrix([[0,0,0,1],[0,0,1,1],[0,1,1,1]])
    assert solver.leftMostColumnWithOne(binaryMatrix) == 1
