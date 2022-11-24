from collections import defaultdict, deque
N, M = (int(x) for x in input().split())

g = defaultdict(list)
for i in range(M):
  s, t = (int(x)-1 for x in input().split())
  g[s].append((i, t))


def solve(g, exclude, N):
  q = deque()
  prevs = [None] * N
  q.append((0,0, None, None))
  visited = set()
  visited.add(0)
  while len(q) > 0:
    n, d, prev, edge = q.popleft()
    prevs[n] = (prev, edge)

    if n == N-1:
      return d, prevs

    for i, nb in g[n]:
      if i == exclude or nb in visited:
        continue

      visited.add(nb)
      q.append((nb, d+1, n, i))
    
  return -1, prevs

dist, prevs = solve(g, -1, N)
if dist == -1:
  for i in range(M):
    print(-1)

  exit()

paths = set()
if dist >= 0:
  p = N-1
  while p is not None:
    p, edge = prevs[p] 
    paths.add(edge)

for i in range(M):
  if i not in paths:
    print(dist)
  else:
    ans, _ = solve(g, i, N)
    print(ans)