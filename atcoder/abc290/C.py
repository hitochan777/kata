N, K = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
A.sort()
ans = 0
prev = None
cnt = 0
i = 0
while cnt < K and i < len(A):
  if A[i] != prev and A[i] == ans:
    ans += 1
    cnt += 1

  prev = A[i]
  i += 1

print(ans)