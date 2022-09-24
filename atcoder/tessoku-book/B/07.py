T = int(input())
N = int(input())
A = [0] * (T + 1)
for _ in range(N):
  L, R = (int(x) for x in input().split())
  A[L] += 1
  A[R] -= 1

for i in range(1, T+1):
  A[i] += A[i-1]

for i in range(T):
  print(A[i])

