from bisect import bisect_left

N, M = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
A.sort()

# 1 2 5 6 6
ans = 0
for i in range(N):
  x = A[i]
  idx = bisect_left(A, x + M)
  ans = max(idx - i, ans)

print(ans)
