from collections import Counter

N = int(input())
cnt = Counter(int(x) for x in input().split())
total = sum(k * v for k, v in cnt.items())
Q = int(input())
for _ in range(Q):
  B, C = (int(x) for x in input().split())
  total += (C - B) * cnt[B]
  cnt[C] += cnt[B]
  cnt[B] = 0
  print(total)