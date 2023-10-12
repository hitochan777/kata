from bisect import bisect_left
N, M, D = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
B = list(int(x) for x in input().split())
A.sort()

ans = -1
for b in B:
  idx = bisect_left(A, b+D+1)
  if idx > 0 and A[idx-1] >= b-D:
    ans = max(A[idx-1] + b, ans)

print(ans)

# 2 * b - D <= a + b <= 2 * b + D 