N = int(input())
A = []
for _ in range(N):
  A.append(int(input()))

ans = 0
for i in range(N-1):
  ans += A[i] // 2
  A[i] %= 2
  d = min(A[i], A[i+1])
  ans += d
  A[i] -= d
  A[i+1] -= d

ans += A[-1] // 2
print(ans)
