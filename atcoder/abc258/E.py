from bisect import bisect_left
from collections import defaultdict

N, Q, X = (int(x) for x in input().split())
W = list(int(x) for x in input().split())
idx = defaultdict(int)
base_cnt = 0
sw = sum(W)
if sw <= X:
  base_cnt = (X // sw) * N 
  X %= sw
  
acc = [0]
for w in (W + W):
  acc.append(acc[-1] + w)

start_idx = 0
start_idx_set = set()
start_idx_set.add(0)
# print(acc, X)
C = []
m = {}
while True:
  if start_idx in m:
    repeat_start_idx = m[start_idx]
    break

  m[start_idx] = len(C)
  target = X + acc[start_idx]
  idx = bisect_left(acc, target)
  C.append(idx - start_idx)
  # print(C, idx, target)
  start_idx = idx % N
  
# print(repeat_start_idx, C)
for _ in range(Q):
  K = int(input()) - 1
  if K <= repeat_start_idx:
    print(C[K] + base_cnt)
  else:
    i = (K - repeat_start_idx) % (len(C) - repeat_start_idx) + repeat_start_idx
    print(C[i] + base_cnt)