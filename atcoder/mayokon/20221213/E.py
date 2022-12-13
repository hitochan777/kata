from collections import defaultdict, deque

def reachable(s, g, N):
  q = deque()
  visited = set()
  q.append(s)
  visited.add(s)
  while len(q) > 0:
    n = q.popleft()
    for nb in g[n]:
      if nb in visited:
        continue
      
      q.append(nb)
      visited.add(nb)

  return len(visited) == N


N = int(input())
ps = []
for i in range(N):
  x, y, P = (int(x) for x in input().split())
  ps.append((i,x,y,P))

ng, ok = -1, 10**18
while ok - ng > 1:
  S = (ok+ng) >> 1
  g = defaultdict(list)
  for i, xi, yi, Pi in ps:
    for j, xj, yj, Pj in ps:
      if Pi*S >= abs(xi-xj) + abs(yi-yj):
        g[i].append(j)


  if any(reachable(i, g, N) for i in range(N)):
    ok = S
  else:
    ng = S
    
print(ok)