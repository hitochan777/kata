from atcoder.dsu import DSU
from collections import Counter
N, M = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
total = sum(A)

cnt = Counter(A)
values = sorted(cnt.keys())

dsu = DSU(len(values))
for i, x in enumerate(values):
  y = (x + 1) % M
  if y in cnt:
    dsu.merge(i, 0 if x+1>=M else i+1)


ans = 0
# print(values)
for group in dsu.groups():
  # print(group)
  s = sum(cnt[values[val]]*values[val] for val in group)
  ans = max(ans, s)

# print(ans, total)

print(total - ans)