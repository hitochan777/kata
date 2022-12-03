from atcoder.dsu import DSU

N = int(input())
A = list(int(x) for x in input().split())
dsu = DSU(max(A)+1)
if N == 1:
  print(0)
  exit()

ans = 0
for i in range(N>>1):
  if not dsu.same(A[i],A[N-i-1]):
    dsu.merge(A[i],A[N-i-1])
    ans += 1
  
print(ans)