N, P, Q, R, S = (int(x) for x in input().split())
A = list(int(x) for x in input().split())

for i in range(Q-P+1):
  A[i+P-1], A[i+R-1] = A[i+R-1], A[i+P-1]

print(*A)
