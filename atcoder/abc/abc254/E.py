from collections import defaultdict, deque

def solve(g, start):
  q = deque()
  q.append((0, start))
  nodes = set()
  while len(q) > 0:
    d, node = q.popleft()
    nodes.add(node)
    if d + 1 <= k:
      for nb in g[node]:
        q.append((d+1, nb))

  return sum(nodes)

N, M = (int(x) for x in input().split())
g = defaultdict(list)
for _ in range(M):
  a, b = (int(x) for x in input().split())
  g[a].append(b)
  g[b].append(a)

Q = int(input())
for _ in range(Q):
  x, k = (int(x) for x in input().split())
  ans = solve(g, x) 
  print(ans)