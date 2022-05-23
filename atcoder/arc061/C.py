from collections import defaultdict

cnt = defaultdict(int)
N, K = (int(x) for x in input().split())
for _ in range(N):
  a, b = (int(x) for x in input().split())
  cnt[a] += b

for i in range(1, 10**5+1):
  K -= cnt[i]
  if K <= 0:
    print(i)
    break