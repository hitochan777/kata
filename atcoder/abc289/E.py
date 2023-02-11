from collections import defaultdict, deque 
import sys
from atcoder.dsu import DSU

input = sys.stdin.readline
T = int(input())

def solve():
  g = defaultdict(list)
  q = deque()
  N, M = (int(x) for x in input().split())
  C = list(int(x) for x in input().split())
  dsu = DSU(N)
  for _ in range(M):
    u, v = (int(x)-1 for x in input().split())
    g[u].append(v)
    g[v].append(u)
    dsu.merge(u, v)

  if not dsu.same(0, N-1):
    return -1

  ans = 10**18
  q.appendleft((0, N-1, 0))
  visited = set() 
  while len(q) > 0:
    n, m, d = q.pop()
    if n == N-1 and m == 0:
      ans = min(ans, d)
      return ans

    for n2 in g[n]:
      for m2 in g[m]:
        if (n2, m2) in visited:
          continue

        visited.add((n2,m2))
        if C[n2] == C[m2]:
          continue

        q.appendleft((n2, m2, d+1))

  if ans == 10**18:
    return -1
  else:
    return ans

for _ in range(T):
  ans = solve()
  sys.stdout.write(f"{ans}\n")
