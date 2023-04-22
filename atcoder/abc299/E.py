from collections import defaultdict, deque

N, M = (int(x) for x in input().split())
g = defaultdict(set)
dist = defaultdict(lambda: defaultdict(int))
for _ in range(M):
    u, v = (int(x)-1 for x in input().split())
    g[u].add(v)
    g[v].add(u)

K = int(input())
white_dist = defaultdict(lambda: -1)
constraints = []
for _ in range(K):
    p, d = (int(x) for x in input().split())
    p -= 1
    white_dist[p] = d-1
    constraints.append((p, d))


whites = set()
for i in range(N):
    visited = set()
    q = deque()
    q.appendleft((i, 0))
    visited.add(i)
    while len(q) > 0:
      n, d = q.pop()
      dist[i][n] = d
      if d <= white_dist[i]:
         whites.add(n)

      for nb in g[n]:
        if nb in visited:
           continue

        q.appendleft((nb, d+1))
        visited.add(n)


for p, d in constraints:
  if all(n in whites for n, d2 in dist[p].items() if d2 == d):
     print("No")
     exit()

print("Yes")
print("".join(["0" if i in whites else "1" for i in range(N)]))