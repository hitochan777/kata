# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, h = 1, n
        while l < h:
            m = (l + h) >> 1
            if isBadVersion(m):
                h = m
            else:
                l = m + 1
                
        return l


if __name__ == "__main__":
    assert Solution([False, False, True, True, True]).firstBadVersion2(5) == 3
    assert Solution([True, True, True]).firstBadVersion2(3) == 1
