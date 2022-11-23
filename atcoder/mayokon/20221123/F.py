from collections import defaultdict, deque
N, M = (int(x) for x in input().split())

g = defaultdict(list)
for i in range(M):
  s, t = (int(x)-1 for x in input().split())
  g[s].append((i, t))


def solve(g, exclude, N):
  q = deque()
  q.append((0,0))
  visited = set()
  visited.add(0)
  while len(q) > 0:
    n, d = q.popleft()
    if n == N-1:
      return d

    for i, nb in g[n]:
      if i == exclude or nb in visited:
        continue

      visited.add(nb)
      q.append((nb, d+1))
    
  return -1

for i in range(M):
  ans = solve(g, i, N)
  print(ans)
