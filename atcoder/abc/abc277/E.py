from collections import deque, defaultdict

N, M, K = (int(x) for x in input().split())
g = defaultdict(list)
for _ in range(M):
  u, v, a = (int(x) for x in input().split())
  u, v = u-1, v-1
  g[(u, 1-a)].append(((v, 1-a), 1))
  g[(v, 1-a)].append(((u, 1-a), 1))

S = set(int(x)-1 for x in input().split())
for n in S:
  g[(n, 0)].append(((n, 1), 0))
  g[(n, 1)].append(((n, 0), 0))

q = deque()
visited = set()
q.append(((0, 0), 0))
visited.add((0, 0))
dist = defaultdict(lambda: 10**18)
while len(q) > 0:
  n, d = q.popleft()
  dist[n] = d
  for nb, c in g[n]:
    if nb in visited:
      continue

    if c == 0:
      q.appendleft((nb,d))
    else:
      q.append((nb,d+1))

    visited.add(nb)

ans = min(dist[(N-1,0)], dist[(N-1, 1)])
print(ans if ans < 10**18 else -1)