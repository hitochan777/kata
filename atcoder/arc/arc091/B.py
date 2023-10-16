N, K = (int(x) for x in input().split())

if K == 0:
  print(N*N)
  exit()
ans = 0
for b in range(K+1, N+1):
  n = (N+1)//b
  ans += (b-K)*n
  L = K+b*n
  R = N
  if  L <= R:
    ans += R - L + 1 

print(ans)