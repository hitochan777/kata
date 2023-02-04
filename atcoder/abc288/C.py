from atcoder.dsu import DSU
from collections import defaultdict

N, M = (int(x) for x in input().split())
cnt = defaultdict(int)
dsu = DSU(N)
edges = []
for _ in range(M):
  A, B = (int(x)-1 for x in input().split())
  prev = dsu.leader(A)
  dsu.merge(A, B)
  edges.append((A,B))

for a, b in edges:
  cnt[dsu.leader(a)] += 1

ans = 0
# print(cnt)
for group in dsu.groups():
  # # print(group)
  # print(cnt[dsu.leader(group[0])])
  ans += cnt[dsu.leader(group[0])]-(len(group)-1)

print(ans)
