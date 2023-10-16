from collections import defaultdict
N, M = (int(x) for x in input().split())
g = defaultdict(set)
for i in range(M):
    u, v = (int(x)-1 for x in input().split())
    g[u].add(v)

ans = defaultdict(list)
for i in range(N):
  q = [i]
  visited = set()
  visited.add(i)
  reachables = set()
  while len(q) > 0:
     node = q.pop()
     reachables.add(node)
     for nb in g[node]:
        if nb not in visited:
          visited.add(nb)
          q.append(nb)

  reachables.remove(i)
  for node in reachables:
    if node not in g[i]:
      ans[i].append(node)

print(sum(len(li) for li in ans.values()))

