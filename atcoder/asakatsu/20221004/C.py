N = int(input())
A = list(int(x) for x in input().split())
A.sort()
ans = 0
for i in range(1,N+1):
  # print(A[3*N-2*i])
  ans += A[3*N-2*i]

print(ans)