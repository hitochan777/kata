from collections import defaultdict, Counter
N = int(input())
cnt = Counter(int(x) for x in input().split())
Q = int(input())
total = sum(k*v for k, v in cnt.items())
for _ in range(Q):
  B, C = (int(x) for x in input().split())
  cnt[C] += cnt[B]
  total += cnt[B] * C - cnt[B] * B
  cnt[B] = 0
  print(total)