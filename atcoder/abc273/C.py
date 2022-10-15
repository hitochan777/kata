from bisect import bisect_left, bisect_right
from collections import defaultdict
from typing import Counter


N = int(input())
A = list(int(x) for x in input().split())
ca = Counter(A)
A = sorted(list(set(A)))
cnt = defaultdict(int)
for i, a in enumerate(A):
  idx = bisect_left(A, a+1)
  # print(len(A)-idx)
  cnt[len(A) - idx] += ca[a]

for i in range(N):
  print(cnt[i])