from atcoder.segtree import SegTree
W, N = (int(x) for x in input().split())

def make_array(*args, default=int):
  if len(args) == 0:
    return default()

  return [make_array(*args[1:], default=default) for _ in range(args[0])]

dishes = []
for _ in range(N):
  L, R, V = (int(x) for x in input().split())
  dishes.append((L, R, V))
  
MAX_SPICE = W + 1
dp = make_array(N+1, MAX_SPICE, default=lambda: -10**18)
dp[0][0] = 0
for i in range(N):
  l, r, v = dishes[i]
  for j in range(MAX_SPICE):
    dp[i+1][j] = dp[i][j]

  st = SegTree(lambda a, b: max(a,b), -10**18, [dp[i][j] for j in range(MAX_SPICE)])
  for j in range(MAX_SPICE):
    cl, cr = max(0, j-r), max(0, j-l+1)
    if cl == cr:
      continue

    mx = st.prod(cl, cr)
    if mx == -10**18:
      continue

    dp[i+1][j] = max(dp[i+1][j], mx + v)

print(dp[N][W] if dp[N][W] != -10**18 else -1)