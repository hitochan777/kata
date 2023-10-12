from collections import deque

H, W = (int(x) for x in input().split())
g = []
for _ in range(H):
  S = list(input())
  g.append(S)

def gen():
  for h in range(H):
    for w in range(W):
      if g[h][w] == ".":
        yield (h, w)

def hash(h, w):
  return h * W + w

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def solve(start, goal):
  sh, sw = start
  gh = hash(*goal)
  visited = set()
  q = deque()
  q.appendleft((hash(sh, sw), 0))
  visited.add(hash(sh, sw))
  while q:
    hashed, d = q.pop()
    if hashed == gh:
      return d

    h, w = hashed // W, hashed % W

    for dh, dw in dirs:
      nh = h + dh
      nw = w + dw
      new_hashed = hash(nh, nw)
      if not (0 <= nh < H and 0 <= nw < W) or new_hashed in visited or g[nh][nw] == "#":
        continue

      visited.add(new_hashed)
      q.appendleft((new_hashed, d+1))

  return -1

ans = 0
solved = set()
for start in gen():
  for goal in gen():
    if (min(start, goal), max(start, goal)) not in solved:
      solved.add((min(start, goal), max(start, goal)))
      ans = max(solve(start, goal), ans)

print(ans)