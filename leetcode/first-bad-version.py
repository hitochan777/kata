class Solution:
    def __init__(self, versions):
        self.versions = versions

    def isBadVersion(self, i):
        return self.versions[i-1]

    def firstBadVersion2(self, n):
        l, h = 1, n + 1
        while l < h:
            m = (l + h) >> 1
            if self.isBadVersion(m):
                h = m - 1
            else:
                l = m + 1

        print(l + 1)
        return l + 1

if __name__ == "__main__":
    assert Solution([False, False, True, True, True]).firstBadVersion2(5) == 3
    assert Solution([True, True, True]).firstBadVersion2(3) == 1
