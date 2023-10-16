N = int(input())
A = list(int(x) for x in input().split())
S = input()

def make_array(*args, default=int):
  if len(args) == 0:
    return default()

  return [make_array(*args[1:]) for _ in range(args[0])]

def get_mex(num):
  nums = set()
  for i in range(1, 4):
    if (num >> i) & 1 == 1:
      nums.add(i-1)

  for i in range(4):
    if i not in nums:
      return i

mex = "MEX"
dp = make_array(N+1, 4, 1<<4)
dp[0][0][0] = 1
for i in range(N):
  for j in range(4):
    for k in range(1<<4):
      dp[i+1][j][k] += dp[i][j][k]
      if j <= 2 and S[i] == mex[j]: 
        dp[i+1][j+1][k | 1 << (A[i]+1)] += dp[i][j][k]


ans = 0
for i in range(1<<4):
  m = get_mex(i)
  ans += m * dp[N][3][i]

print(ans)