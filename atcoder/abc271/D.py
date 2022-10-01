N, S = (int(x) for x in input().split())
dp = [[(False, None)]*(S+1) for _ in range(N+1) ]
cards = []
for _ in range(N):
  a, b = (int(x) for x in input().split())
  cards.append([a,b])

dp[0][0] = (True, None)

for i in range(N):
  for j in range(S+1):
    if j >= cards[i][0] and dp[i][j-cards[i][0]][0]:
      dp[i+1][j] = (True, 0) 
    elif j >= cards[i][1] and dp[i][j-cards[i][1]][0]:
      dp[i+1][j] = (True, 1)

if not dp[N][S][0]:
  print("No")
  exit()

print("Yes")
ans = []
b = S
for i in range(N, 0, -1):
  _, side = dp[i][b]
  b -= cards[i-1][side]
  ans.append("H" if side == 0 else "T")

print("".join(ans[::-1]))