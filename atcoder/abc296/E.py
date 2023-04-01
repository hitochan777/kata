from atcoder.scc import SCCGraph
from collections import defaultdict
N = int(input())
A = list(int(x)-1 for x in input().split())
g = SCCGraph(N)
self_edge = set()
for i, a in enumerate(A):
  # print(i,a)
  g.add_edge(i, a)
  if i == a:
    self_edge.add(i)

scc = g.scc()
is_scc = set()
# print(scc)

for group in scc:
  for n in group:
    if len(group) >= 2 or n in self_edge:
      is_scc.add(n)

# print(is_scc)

cnt = 0
for i in range(N):
  if i in is_scc:
    cnt += 1

print(cnt)