N, K, Q = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
L = list(int(x)-1 for x in input().split())
for l in L:
  if A[l] == N:
    continue
  
  if l == K-1:
    A[l] += 1
    continue
  
  if A[l+1] - A[l] == 1:
    continue
  
  A[l] += 1
  
print(*A)