from collections import defaultdict, deque
N = int(input())
g = defaultdict(list)
edges = []
for _ in range(N-1):
  a, b = (int(x)-1 for x in input().split())
  g[a].append(b)
  g[b].append(a)
  edges.append((a,b))

q = [(0,-1)]
parents = {}
while len(q) > 0:
  node, parent = q.pop()
  parents[node] = parent
  children = 0
  for nb in g[node]:
    if nb == parent:
      continue

    children += 1
    q.append((nb, node))

scores = defaultdict(int)
Q = int(input())
for _ in range(Q):
  t, e, x = (int(x) for x in input().split())
  avoid = edges[e-1][t%2]
  node = edges[e-1][(t+1)%2]
  if parents[node] == avoid:
    scores[node] += x
  else:
    scores[0] += x
    scores[avoid] -= x

q = deque()
q.append((0, scores[0]))
while len(q) > 0:
  node, score = q.popleft()
  scores[node] = score
  for nb in g[node]:
    if nb == parents[node]:
      continue

    q.append((nb, score+scores[nb]))

for i in range(N):
  print(scores[i])