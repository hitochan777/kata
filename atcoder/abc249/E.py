from collections import namedtuple


from typing import List
N, K = (int(x) for x in input().split())
Operation = namedtuple("Operation", ["t", "y"])
x = 0
diffs = []
ops: List[Operation] = []
for i in range(N):
  t, y = (int(x) for x in input().split())
  ops.append(Operation(t, y))
  diff = y - x if t == 1 else y
  diffs.append((diff, i))
  x += diffs[-1][0]

diffs.sort(reverse=True)
for i in range(N-1, -1, -1):

