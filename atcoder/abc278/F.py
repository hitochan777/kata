N = int(input())
S = []
NUM=26
for _ in range(N):
  S.append(input())

dp = [[False]*NUM for _ in range(1<<N)]

def atoi(c):
  return ord(c) - ord("a")

for i in range(1<<N):
  for c in range(NUM):
    for j in range(N):
      # print(i & ((1<<j)^((1<<N)-1)))
      if (i>>j) & 1 == 1 and atoi(S[j][0]) == c and not dp[i & ((1<<j)^((1<<N)-1))][atoi(S[j][-1])]:
        dp[i][c] = True
        break

# for row in dp:
#   print(row)

if any(dp[(1<<N)-1]):
  print("First")
else:
  print("Second")