N, K, X = (int(x) for x in input().split())
A = list(int(x) for x in input().split())

cost = 0
for i in range(N):
  a = A[i]
  k = a // X
  k = min(k, K)
  A[i] = a - k * X
  K -= k

A.sort(reverse=True)
i = 0
for i in range(N):
  if K > 0:
    A[i] = max(A[i] - X, 0)
    K -= 1

print(sum(A))
