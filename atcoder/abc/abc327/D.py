from collections import deque
from collections import defaultdict

N, M = list(map(int,input().split()))
g = defaultdict(set)
A = list(int(x) for x in input().split())
B = list(int(x) for x in input().split())
for a, b in zip(A, B):
  g[a].add(b)
  g[b].add(a)

def is_bipartile(g, N):
  color = [0 for i in range(N+1)]
  color[1] = 1
  q = deque([1])
  while len(q):
    p = q.popleft()
    for nb in list(g[p]):
      if color[nb] == 0:
        color[nb] = -color[p]
        q.append(nb)
      elif color[nb] == color[p]:
        return False

  return True

if is_bipartile(g, N):
  print("Yes")
else:
  print("No")