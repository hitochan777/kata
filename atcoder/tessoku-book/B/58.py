from atcoder.segtree import SegTree
from bisect import bisect_left
N, L, R = (int(x) for x in input().split())
X = list(int(x) for x in input().split())

dp = [10**18] * N
dp[0] = 0

st = SegTree(lambda x,y: min(x,y), 10**18, dp)

for i in range(1, N):
  l = bisect_left(X, X[i]-R)
  r = bisect_left(X, X[i]-L)
  # if X[i] - R < X[l]:
  #   l += 1

  if X[i] - L < X[r]:
    r -= 1

  dp[i] = st.prod(l, r+1) + 1
  st.set(i, dp[i])

print(dp[N-1])