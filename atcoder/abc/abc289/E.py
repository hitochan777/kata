from collections import defaultdict, deque 
import sys

input = sys.stdin.readline
T = int(input())

def solve():
  g = defaultdict(list)
  q = deque()
  N, M = (int(x) for x in input().split())
  C = list(int(x) for x in input().split())
  for _ in range(M):
    u, v = (int(x)-1 for x in input().split())
    g[u].append(v)
    g[v].append(u)

  q.appendleft((0, N-1, 0))
  visited = set()
  while len(q) > 0:
    n, m, d = q.pop()
    if n == N-1 and m == 0:
      return d

    for n2 in g[n]:
      for m2 in g[m]:
        key = n2 * 10000 + m2
        # using tuple as key make set operation slow
        # key = (n2, m2)
        if C[n2] == C[m2] or key in visited:
          continue

        visited.add(key)

        q.appendleft((n2, m2, d+1))

  return -1

for _ in range(T):
  ans = solve()
  sys.stdout.write(f"{ans}\n")
