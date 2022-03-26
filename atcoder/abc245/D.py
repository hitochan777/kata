N, M = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
C = list(int(x) for x in input().split())
B = [0] * (M + 1)
for k in range(M+1):
  total = sum(A[N-i] * B[M-(k-i)] for i in range(min(N, k)+1))
  diff = C[N+M-k] - total
  B[M-k] =  diff // A[N]

print(*B)
