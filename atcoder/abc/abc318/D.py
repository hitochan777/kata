from collections import defaultdict
N = int(input())
g = defaultdict(lambda: defaultdict(set))
for i in range(N-1):
  D = list(int(x) for x in input().split())
  for j, d in enumerate(D):
    g[i][i+j+1] = d
    g[i+j+1][i] = d

def dfs(used):
  a = None
  for i in range(N):
    if i not in used:
      a = i
      break

  if a is None:
    return 0

  used.add(a)
  ans = 0
  for nb in range(N):
    if nb not in used:
      used.add(nb)
      ans = max(ans, g[a][nb] + dfs(used))
      used.remove(nb)

  used.remove(a)
  return ans

if N % 2 == 0:
  used = set()
  ans = dfs(used)
  print(ans)
else:
  ans = 0
  for i in range(N):
    used = set()
    used.add(i)
    ans = max(ans, dfs(used))

  print(ans)

