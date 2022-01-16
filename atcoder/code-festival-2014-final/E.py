N = int(input())
R = list(int(x) for x in input().split())

def make_array(*args):
  if len(args) == 0:
    return 1 

  return [make_array(*args[1:]) for _ in range(args[0])]

dp = make_array(N+1, 2)
dp[0] = [0,0]

for i in range(N+1):
  for j in range(0, i):
    for d in range(2):
      if d == 0:
        if R[i-1] < R[j-1]:
          dp[i][1] = max(dp[i][1], dp[j][0] + 1)
      else:
        if R[i-1] > R[j-1]:
          dp[i][0] = max(dp[i][0], dp[j][1] + 1)

print(dp)

ans = max(dp[i][j] for i in range(N+1) for j in range(2))
print(ans)