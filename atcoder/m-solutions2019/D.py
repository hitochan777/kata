from collections import defaultdict


N = int(input())
g = defaultdict(list)
for _ in range(N-1):
  a, b = (int(x)-1 for x in input().split())
  g[a].append(b)
  g[b].append(a)

leaf = None
for n, nbs in g.items():
  if len(nbs) == 1:
    leaf = n
    break

nums = [None] * N
C = list(int(x) for x in input().split())
C.sort()
ans = sum(C[:-1])

q = [(leaf, None)]
while len(q) > 0:
  node, parent = q.pop()
  nums[node] = C.pop()
  for nb in g[node]:
    if nb == parent:
      continue

    q.append((nb, node))

print(ans)
print(*nums)


