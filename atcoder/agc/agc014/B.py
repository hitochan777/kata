from collections import defaultdict


N, M = (int(x) for x in input().split())
cnt = defaultdict(int)
for _ in range(M):
  a, b = (int(x) for x in input().split())
  cnt[a] += 1
  cnt[b] += 1

if all(v % 2 == 0 for v in cnt.values()):
  print("YES")
else:
  print("NO")