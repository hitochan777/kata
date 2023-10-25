from collections import defaultdict

g = defaultdict(set)
cnt_inc_edges = defaultdict(int)
N, M = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
for _ in range(M):
  X, Y = (int(x)-1 for x in input().split())
  g[X].add(Y)
  cnt_inc_edges[Y] += 1

root_nodes = set()
for i in range(N):
  if cnt_inc_edges[i] == 0:
    root_nodes.add(i)

L = []
while root_nodes:
  n = root_nodes.pop()
  L.append(n)
  for nb in g[n]:
    cnt_inc_edges[nb] -= 1
    if cnt_inc_edges[nb] == 0:
      root_nodes.add(nb)

# print(L)
min_price = defaultdict(lambda: 10**18)
ans = -10**18
for n in L:
  # print(n, A[n], min_price[n])
  ans = max(ans, A[n] - min_price[n])
  for nb in g[n]:
    min_price[n] = min(min_price[n], A[n])
    min_price[nb] = min(min_price[nb], min_price[n])

print(ans)

