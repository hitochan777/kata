from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
N = int(input())
g = defaultdict(list)
for _ in range(N-1):
  u, v = (int(x)-1 for x in input().split())
  g[u].append(v)
  g[v].append(u)


ans = [None] * N
def dfs(n, start=0, parent=-1):
  global ans
  end = start
  p = start
  for nb in g[n]:
    if nb == parent:
      continue

    end = dfs(nb, p, n)
    p = end + 1

  ans[n] = [start+1, end+1]
  return end

dfs(0)
for l, r in ans:
  print(l, r)