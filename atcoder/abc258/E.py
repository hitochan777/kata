from bisect import bisect_left
from collections import defaultdict

N, Q, X = (int(x) for x in input().split())
W = list(int(x) for x in input().split())
idx = defaultdict(int)
base_cnt = 0
sw = sum(W)
if sw >= X:
  base_cnt = (X // sw) * N
  X %= sw
  
acc = [0]
for w in W:
  acc.append(acc[-1] + w)

start_idx = 0
start_idx_set = set()
start_idx_set.add(0)
C = []
while True:
  target = X + acc[start_idx]
  idx = bisect_left(acc, target)
  if idx >= N+1:
    idx = bisect_left(acc, X - (acc[-1] - acc[start_idx]))
    
  C.append(N if idx == start_idx else idx - start_idx)
  if idx in start_idx_set:
    repeat_start_idx = idx
    break

  start_idx = idx
  start_idx_set.add(idx)
  

for _ in range(Q):
  K = int(input()) - 1
  if K <= repeat_start_idx:
    print(C[K] + base_cnt)
  else:
    i = (K - repeat_start_idx) % len(C) + repeat_start_idx
    print(C[i] + base_cnt)