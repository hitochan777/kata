from atcoder.fenwicktree import FenwickTree
N = int(input())
A = list(int(x) for x in input().split())

bit = FenwickTree(10**6)
inversion = 0
for i, a in enumerate(A):
  inversion += i - bit.sum(0, a)
  bit.add(a, 1)

print(inversion)
for i in range(N-1):
  inversion += N - 1 - 2 * A[i]
  print(inversion)
