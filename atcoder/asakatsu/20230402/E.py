from collections import deque, defaultdict
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
H, W = (int(x) for x in input().split())
g = []
warps = defaultdict(list)
warped = set()
S = None
for i in range(H):
  g.append(input())
  for j, c in enumerate(g[-1]):
    if c.isalpha() and c.islower():
      warps[c].append((i, j))

    if c == "S":
      S = (i, j)

# print(warps)
def hash(i, j):
  return i * W + j

q = deque()
q.appendleft((S[0], S[1], 0))
visited = set()
visited.add(hash(S[0], S[1]))
while len(q) > 0:
  x, y, dist = q.pop()
  if g[x][y] == "G":
    print(dist)
    exit()

  for dx, dy in dirs:
    if 0 <= x+dx < H and 0 <= y+dy < W and g[x+dx][y+dy] != "#" and hash(x+dx, y+dy) not in visited:
      q.appendleft((x+dx, y+dy, dist+1))
      visited.add(hash(x+dx, y+dy))

  if g[x][y] not in warped:
    warped.add(g[x][y])
    for x1, y1 in warps[g[x][y]]:
      if hash(x1, y1) not in visited:
        q.appendleft((x1, y1, dist+1))
        visited.add(hash(x1, y1))

print(-1)
