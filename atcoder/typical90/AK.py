from atcoder.segtree import SegTree
W, N = (int(x) for x in input().split())

def make_array(*args, default=int):
  if len(args) == 0:
    return default()

  return [make_array(*args[1:]) for _ in range(args[0])]

dishes = []
for _ in range(N):
  L, R, V = (int(x) for x in input().split())
  dishes.append((L, R, V))
  
MAX_SPICE = W + 1
dp = make_array(N+1, MAX_SPICE)

for i in range(N):
  l, r, v = dishes[i]
  st = SegTree(lambda a, b: max(a,b), 0, [dp[i][j] + v for j in range(MAX_SPICE)])
  for j in range(MAX_SPICE):
    dp[i+1][j] = dp[i][j]
    l, r = max(0, j-l), max(0, j-r+1)
    if l > r:
      continue

    mx = st.prod(l, r)
    dp[i+1][j] = max(dp[i+1][j], mx)

print(dp[N][W])