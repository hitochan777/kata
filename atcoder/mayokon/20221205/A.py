N = int(input())
A = list(int(x) for x in input().split())
ans = 0
for i in range(N):
  for j in range(N):
    ans = max(ans, abs(A[i]-A[j]))

print(ans)
  