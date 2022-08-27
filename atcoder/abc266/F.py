from collections import defaultdict
from itertools import cycle
import sys

sys.setrecursionlimit(10**6)

N = int(input())
g = defaultdict(list)

for _ in range(N):
  u, v = (int(x)-1 for x in input().split())
  g[u].append(v)
  g[v].append(u)

cycle = set()
visited = set()
def find_cycle(node):
  global cycle
  visited.add(node)
  for nb in g[node]:
    if nb in visited:
      for n in visited:
        cycle.add(n)
      print(cycle)
      return
    
    find_cycle(nb)

  visited.remove(node)
  return

find_cycle(0)
print(cycle)

Q = int(input())
for _ in range(Q):
  x, y = (int(x)-1 for x in input().split())
  if x in cycle and y in cycle:
    print("No")
  else:
    print("Yes")