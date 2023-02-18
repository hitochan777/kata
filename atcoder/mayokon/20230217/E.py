import sys
from collections import defaultdict
from atcoder.fenwicktree import FenwickTree

N, Q = (int(x) for x in input().split())
C = list(int(x)-1 for x in sys.stdin.readline().split())
ranges = []
for i in range(Q):
    l, r = (int(x) for x in sys.stdin.readline().split())
    ranges.append((i, l, r))

ranges.sort(key=lambda x: x[2])

ans = [None] * Q
fw = FenwickTree(N)
last_index = defaultdict(int)
i = 0
for p, l, r in ranges:
  while i < r:
    if C[i] in last_index:
      fw.add(last_index[C[i]], -1)

    last_index[C[i]] = i
    fw.add(last_index[C[i]], 1)
    i += 1

  ans[p] = fw.sum(l-1, r)

for val in ans:
   sys.stdout.write(str(val)+"\n")
  
