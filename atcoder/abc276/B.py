from collections import defaultdict

N, M = (int(x) for x in input().split())
cnt = defaultdict(list)
for _ in range(M):
  A, B = (int(x) for x in input().split())
  cnt[A].append(B)
  cnt[B].append(A)

for i in range(1,N+1):
  a = [len(cnt[i])] + sorted(cnt[i])
  print(*a)