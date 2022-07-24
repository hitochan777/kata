from collections import defaultdict
from atcoder.fenwicktree import FenwickTree

N = int(input())
C = list(int(x) for x in input().split())
cs = set(C)
X = list(int(x) for x in input().split())
ft = FenwickTree(N+1)
ans = 0
for i, x in enumerate(X):
  ans += ft.sum(x+1, N+1)
  ft.add(x, 1)

X_by_color = defaultdict(list)
for x, c in zip(X, C):
  X_by_color[c].append(x)

for xs in X_by_color.values():
  # for coordinate compression
  compress_dict = { x:i for i, x in enumerate(sorted(list(set(xs))))}
  ft2 = FenwickTree(len(compress_dict))
  swapped = 0
  for x in xs:
    swapped += ft2.sum(compress_dict[x]+1, len(compress_dict)) 
    ft2.add(compress_dict[x], 1)

  ans -= swapped

print(ans)