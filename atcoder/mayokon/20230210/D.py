from atcoder.dsu import DSU
N, M = (int(x) for x in input().split())
edges = []
ans = 0
for _ in range(M):
    A, B, C = (int(x) for x in input().split())
    A, B = A-1, B-1
    edges.append((C, A, B))
    if C > 0:
        ans += C

edges.sort()
dsu = DSU(N)
for c, a, b in edges:
    if dsu.same(a, b):
        continue

    if c > 0:
        ans -= c

    dsu.merge(a, b)

print(ans)
