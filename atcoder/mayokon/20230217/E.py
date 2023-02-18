from collections import defaultdict
from atcoder.fenwicktree import FenwickTree

N, Q = (int(x) for x in input().split())
C = list(int(x)-1 for x in input().split())
ranges = []
for i in range(Q):
    l, r = (int(x) for x in input().split())
    ranges.append((r,l,i))

ranges.sort()

ans = []
fw = FenwickTree(N)
last_index = defaultdict(int)
i = 0
for r, l, p in ranges:
  while i < r:
    if C[i] in last_index:
      fw.add(last_index[C[i]], -1)

    last_index[C[i]] = i
    fw.add(last_index[C[i]], 1)
    i += 1

  ans.append((p, fw.sum(l-1, r)))

ans.sort()
for _, val in ans:
   print(val)
  
