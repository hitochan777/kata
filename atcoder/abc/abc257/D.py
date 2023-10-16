from collections import deque


N = int(input())
jumpers = []
for _ in range(N):
  x, y, P = (int(x) for x in input().split())
  jumpers.append((x,y,P))
  
ng, ok = 0, 10**18

def jumpable(s):
  for i in range(N):
    oks = set()
    oks.add(i)
    q = deque()
    q.append(i)
    while len(q) > 0:
      node = q.pop()
      xi, yi, Pi = jumpers[node]
      for j, (xj, yj, _) in enumerate(jumpers):
        if j in oks:
          continue

        if Pi * s >= abs(xi - xj) + abs(yi - yj):
          q.append(j)
          oks.add(j)

    if len(oks) == N:
      return True

  return False

while ok - ng > 1:
  s = (ok + ng) >> 1
  good = jumpable(s)
  if good:
    ok = s
  else:
    ng = s
    
print(ok)