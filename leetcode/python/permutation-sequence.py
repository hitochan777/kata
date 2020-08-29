from math import factorial


class Solution(object):
    def _getPermutation(self, n, k, numbers):
        if n == 0 or k == 0:
            return "".join(map(str, numbers))
        
        f = factorial(n-1)
        return str(numbers[k // f]) + self._getPermutation(n-1, k % f, numbers[:k//f] + numbers[k//f+1:])
    
    def getPermutation(self, n, k):
        return self._getPermutation(n, k-1, list(range(1,n+1)))


def assert_equal(output, expected):
    assert output == expected, f"{output=} {expected=}"

if __name__ == "__main__":
    solver = Solution()
    assert_equal(solver.getPermutation(3, 3), "213")
    assert_equal(solver.getPermutation(3, 2), "132")
    assert_equal(solver.getPermutation(4, 9), "2314")
