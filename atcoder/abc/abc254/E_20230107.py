from collections import defaultdict
g = defaultdict(list)
N, M = (int(x) for x in input().split())
for _ in range(M):
  a, b = (int(x) for x in input().split())
  g[a].append(b)
  g[b].append(a)



def dfs(n, k, visited):
  if n in visited:
    return 0

  if k == 0:
    return n

  total = n
  visited.add(n)
  for nb in g[n]:
    total += dfs(nb, k-1, visited)

  return total

Q = int(input())
for _ in range(Q):
  x, k = (int(x) for x in input().split()) 
  visited = set()
  ans = dfs(x, k, visited)
  print(ans)