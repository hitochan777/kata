from collections import defaultdict

N, T = (int(x) for x in input().split())
C = list(int(x) for x in input().split())
R = list(int(x) for x in input().split())
attrs = defaultdict(list)
for i, (c, r) in enumerate(zip(C, R)):
  attrs[c].append((r, i))

if len(attrs[T]) > 0:
  _, ans = max(attrs[T])
  print(ans+1)
else:
  _, ans = max(attrs[C[0]])
  print(ans+1)