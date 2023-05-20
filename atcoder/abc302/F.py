from collections import defaultdict, deque
N, M = (int(x) for x in input().split())
ss = set()
ones = set()
ms = set()
for _ in range(N):
  _ = int(input())
  S = set(int(x) for x in input().split())
  if 1 in S and M in S:
     print(0)
     exit()

  ss.add(frozenset(S))

g = defaultdict(set)
ss = list(ss)
contains = defaultdict(set)
for i, s in enumerate(ss):
  if 1 in s:
    ones.add(i)

  if M in s:
    ms.add(i)

  for a in s:
    contains[a].add(i)

for s in contains.values():
  for i in s:
     for j in s:
        if i == j:
           continue

        g[i].add(j)
        g[j].add(i)

ans = 10**18
for i in ones:
  q = deque()
  q.appendleft((i, 0))
  visited = set()
  visited.add(i)
  while q:
    node, d = q.pop()
    if node in ms:
       ans = min(ans, d)
       break

    for nb in g[node]:
       if nb not in visited:
          visited.add(nb)
          q.appendleft((nb, d+1))

if ans == 10**18:
   print(-1)
else:
  print(ans)