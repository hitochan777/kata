from math import comb

import bisect

N = int(input())
A = list(int(x) for x in input().split())
A.sort()
max_val = 0
ans = None
for i, a in enumerate(A):
  if a % 2 == 0:
    idx = bisect.bisect_left(A, a // 2)
    idx = min(idx, len(A)-1)
    if i == idx:
      continue

    val = comb(a, A[idx])
    if max_val < val:
      max_val = val 
      ans = (a, A[idx])

  else:
    idx1 = bisect.bisect_left(A, a // 2)
    idx1 = min(idx1, len(A)-1)
    if i == idx1:
      continue

    val = comb(a, A[idx1])
    if max_val < val:
      max_val = val 
      ans = (a, A[idx1])

    idx2 = bisect.bisect_left(A, a // 2 + 1)
    idx2 = min(idx2, len(A)-1)
    if i == idx2:
      continue

    val = comb(a, A[idx2])
    if max_val < val:
      max_val = val 
      ans = (a, A[idx2])

print(*ans) 