def make_array(*args):
  if len(args) == 0:
    return False

  return [make_array(*args[1:]) for _ in range(args[0])]

N, X = (int(x) for x in input().split())
A = []
B = []
for _ in range(N):
  a, b = (int(x) for x in input().split())
  A.append(a)
  B.append(b)

dp = make_array(N+1, X+1)
dp[0][0] = True
for n in range(1,N+1):
  for x in range(X+1):
    for c in range(B[n-1]+1):
      cost = x-c*A[n-1]
      if cost < 0:
        break

      dp[n][x] |= dp[n-1][cost]

print("Yes" if dp[N][X] else "No")
