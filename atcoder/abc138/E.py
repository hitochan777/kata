from bisect import bisect_left 
from collections import defaultdict

s = input()
t = input()
indices = defaultdict(list)

for i, c in enumerate(s+s):
  indices[c].append(i)

p = 0
wrapped = 0
for c in t:
  idx = bisect_left(indices[c], p)
  if idx >= len(indices[c]):
    print(-1)
    exit()

  if indices[c][idx] >= len(s):
    wrapped += 1

  p = indices[c][idx] % len(s)

print(wrapped * len(s) + p + 1)