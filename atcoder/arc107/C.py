import sys
sys.setrecursionlimit(10**5)

def factorial(n, mod):
  if n == 1:
    return 1

  val = n * factorial(n-1, mod)
  return val % mod

  
N, K = (int(x) for x in input().split())
A = []
for _ in range(N):
  A.append(list(int(x) for x in input().split()))


rcnt = 0
for i in range(N):
  for j in range(i+1, N):
    if all(A[i][k] + A[j][k] <= K for k in range(N)):
      rcnt += 1
      
ccnt = 0
for i in range(N):
  for j in range(i+1, N):
    if all(A[k][i] + A[k][j] <= K for k in range(N)):
      ccnt += 1
      
MOD = 998244353
print(rcnt+1, ccnt+1)
ans = (factorial(rcnt+1, MOD) * factorial(ccnt+1, MOD)) % MOD
print(ans)
