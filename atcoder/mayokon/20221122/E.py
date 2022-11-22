from atcoder.segtree import SegTree

N, K = (int(x) for x in input().split())

MOD = 998244353
A = [0] * (N+1)
A[0] = 1
A[1] = -1
ranges = []
for _ in range(K):
  L, R = (int(x) for x in input().split())
  ranges.append((L,R))

for i in range(N-1):
  for L, R in ranges:
    L = min(i+L, N)
    R = min(i+R+1,N)
    A[L] += A[i]
    if L != R:
      A[R] -= A[i]

print(A)

for i in range(N):
  A[i+1] += A[i]
  A[i+1] %= MOD

print(A[N-1])
