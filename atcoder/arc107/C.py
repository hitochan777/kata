import sys
from atcoder.scc import SCCGraph

sys.setrecursionlimit(10**5)
MOD = 998244353

def factorial(n, mod):
  if n == 1:
    return 1

  val = n * factorial(n-1, mod)
  return val % mod


N, K = (int(x) for x in input().split())
A = []
for _ in range(N):
  A.append(list(int(x) for x in input().split()))

ans = 1
scc = SCCGraph(N)
rcnt = 0
for i in range(N):
  for j in range(i+1, N):
    if all(A[i][k] + A[j][k] <= K for k in range(N)):
      scc.add_edge(i, j)
      scc.add_edge(j, i)
      
for nodes in scc.scc():
  ans *= factorial(len(nodes), MOD)
  ans %= MOD
      
ccnt = 0
scc = SCCGraph(N)
for i in range(N):
  for j in range(i+1, N):
    if all(A[k][i] + A[k][j] <= K for k in range(N)):
      scc.add_edge(i, j)
      scc.add_edge(j, i)
      
for nodes in scc.scc():
  ans *= factorial(len(nodes), MOD)
  ans %= MOD
      
print(ans)
