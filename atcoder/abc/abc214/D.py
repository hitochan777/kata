from atcoder.dsu import DSU

N = int(input())
edges = []
for _ in range(N-1):
  u, v, w = (int(x) for x in input().split())
  edges.append((w, u-1, v-1))

edges.sort()

dsu = DSU(N)
ans = 0
for w, u, v in edges:
  ans += w * dsu.size(u) * dsu.size(v)
  dsu.merge(u, v)

print(ans)


