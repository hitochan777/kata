from collections import deque



H, W = (int(x) for x in input().split())
def hash(i, j):
 return i * W + j

def rev_hash(val):
  return (val // W, val % W)

g = []
persons = []
start = None
goal = None
for i in range(H):
  row = list(input())
  for j, c in enumerate(row):
    if c in ">v<^":
      persons.append((c, i, j))
    elif c == "S":
      start = (i, j)
    elif c == "G":
      goal = (i, j)

  g.append(row)

# print(persons)
looked = set()
hori_visited = set()
ver_visited = set()
for c, i, j in persons:
  if c in "<>":
    visited = hori_visited
    if c == "<":
      dir = (0, -1)
    else:
      dir = (0, 1)
  else:
    visited = ver_visited
    if c == "^":
      dir = (-1, 0)
    else:
      dir = (1, 0)
  
  x, y = i+dir[0], j+dir[1]
  while 0 <= x < H and 0 <= y < W and g[x][y] == ".":
    h = hash(x, y)
    if h in visited:
      break

    visited.add(h)
    looked.add(h)
    x, y = x + dir[0], y + dir[1]

# print(looked)
for h in looked:
  x, y = rev_hash(h)
  g[x][y] = "#"

# for row in g:
#   print(row)

q = deque()
sh = hash(*start)
gh = hash(*goal)
q.appendleft((sh, 0))
visited = set()
visited.add(sh)
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while q:
  pos, d = q.pop()
  if pos == gh:
    print(d)
    exit()

  x, y = rev_hash(pos)
  for dx, dy in dirs:
    nx = x + dx
    ny = y + dy
    # print(nx, ny)
    if not (0 <= nx < H and 0 <= ny < W and  hash(nx, ny) not in visited and g[nx][ny] in "G."):
      continue

    visited.add(hash(nx, ny))
    q.appendleft((hash(nx, ny), d+1))


print(-1)