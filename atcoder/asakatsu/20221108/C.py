N, X = (int(x) for x in input().split())
A = []
B = []
for _ in range(N):
  a, b = (int(x) for x in input().split())
  A.append(a)
  B.append(b)

dp = [False] * (X+1)
dp[0] = True
for i in range(N):
  dp2 = [False] * (X+1)
  for j in range(X+1):
    if not dp[j]:
      continue

    if X >= j + A[i]:
      dp2[j + A[i]] = True

    if X >= j + B[i]:
      dp2[j + B[i]] = True

  dp = dp2

print("Yes" if dp[X] else "No")