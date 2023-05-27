from collections import defaultdict, deque
N, M = (int(x) for x in input().split())
ss = []
for _ in range(N):
  _ = int(input())
  S = set(int(x) for x in input().split())
  if 1 in S and M in S:
     print(0)
     exit()

  ss.append(S)

g = defaultdict(set)
for i, s in enumerate(ss):
  for a in s:
    b = N+a-1
    g[i].add(b)
    g[b].add(i)

q = deque()
q.appendleft((N, 0))
visited = set()
visited.add(N)
ans = 10**18
while q:
  node, d = q.pop()
  if node == N + M - 1:
    print(d // 2 - 1)
    exit()

  for nb in g[node]:
    if nb not in visited:
      visited.add(nb)
      q.appendleft((nb, d+1))

print(-1)