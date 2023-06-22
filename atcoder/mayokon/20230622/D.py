from collections import defaultdict
N = int(input())
testimonies = defaultdict(list)
for i in range(N):
  A = int(input())
  for _ in range(A):
    x, y = (int(x) for x in input().split())
    x -= 1
    testimonies[i].append((x,y))

ans = 0
for i in range(1<<N):
  honests = set()
  for j in range(N):
    if (i >> j) & 1:
      honests.add(j)

  for honest in honests:
    if not all((y == 0 and x not in honests) or (y == 1 and x in honests) for x, y in testimonies[honest]):
      break
  else:
    ans = max(ans, len(honests))

print(ans)
      