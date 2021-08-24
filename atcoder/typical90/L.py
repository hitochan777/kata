from atcoder.dsu import DSU

H, W = (int(x) for x in input().split())
H, W = H+2, W+2
Q = int(input())
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def make_array(*args, default=int):
  if len(args) == 0:
    return default()

  return [make_array(*args[1:]) for _ in range(args[0])]

colored = make_array(H, W, default=False)
dsu = DSU(H * W)

for _ in range(Q):
  t, *rest = (int(x) for x in input().split())
  if t == 1:
    r, c = rest
    if colored[r][c]:
      continue

    colored[r][c] = True
    for dr, dc in DIRECTIONS:
      if colored[r+dr][c+dc]:
        dsu.merge((r+dr) * W + c+dc, r * W + c)

  else:
    ra, ca, rb, cb = rest
    if colored[ra][ca] and colored[rb][cb] and dsu.same(ra * W + ca, rb * W + cb):
      print("Yes")
    else:
      print("No")


   