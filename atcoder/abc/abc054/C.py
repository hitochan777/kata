from collections import defaultdict

N, M = (int(x) for x in input().split())
g = defaultdict(list)
for _ in range(M):
  a, b = (int(x)-1 for x in input().split())
  g[a].append(b)
  g[b].append(a)

visited = set()
visited.add(0)
def dfs(node, cnt=0):
  if cnt == N-1:
    return 1

  ans = 0
  for nb in g[node]:
    if nb in visited:
      continue
    
    visited.add(nb)
    ans += dfs(nb ,cnt+1)
    visited.remove(nb)

  return ans

print(dfs(0))