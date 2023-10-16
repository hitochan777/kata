import bisect

N, Q = list(int(x) for x in input().split())
A = list(int(x) for x in input().split())
A.sort()
acc = [0]
for a in A:
  acc.append(acc[-1] + a)

for _ in range(Q):
  X = int(input())
  idx = bisect.bisect_left(A, X)
  # print(idx * X - acc[idx], (acc[N] - acc[idx]) - (N-idx) * X)
  ans = idx * X - acc[idx]  + (acc[N] - acc[idx]) - (N-idx) * X
  print(ans)