class FenwickTree:
    def __init__(self, n):
        self._n = n
        self.data = [0] * n

    def add(self, p, x):
        # assert 0 <= p < self._n
        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p

    def sum(self, l, r):
        # assert 0 <= l <= r <= self._n
        return self._sum(r) - self._sum(l)

    def _sum(self, r):
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r
        return s

N = int(input())
C = list(int(x) for x in input().split())
cs = set(C)
X = list(int(x) for x in input().split())

fd = {}
for c in cs:
  fd[c] = FenwickTree(N+2)

ft = FenwickTree(N+2)

ans = 0
for i, x in enumerate(X):
  ans += ft.sum(x+1, N+1) - fd[C[i]].sum(x+1, N+1)
  ft.add(x, 1)
  fd[C[i]].add(x, 1)

print(ans)