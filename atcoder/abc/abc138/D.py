from collections import defaultdict, deque
g = defaultdict(list)
cnt = defaultdict(int)
N, Q = (int(x) for x in input().split())
for _ in range(N-1):
  a, b = (int(x) for x in input().split())
  a, b = a-1, b-1
  g[a].append(b)
  g[b].append(a)

for _ in range(Q):
  p, x = (int(x) for x in input().split())
  cnt[p-1] += x

q = deque()
q.appendleft((0, -1))
while len(q) > 0:
  node, parent = q.pop()
  for nb in g[node]:
    if nb == parent:
      continue

    cnt[nb] += cnt[node]
    q.appendleft((nb, node))

print(*[cnt[i] for i in range(N)])
   
