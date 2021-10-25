def make_array(*args, default=int):
  if len(args) == 0:
    return default()

  return [make_array(*args[1:], default=default) for _ in range(args[0])]

N, K = (int(x) for x in input().split())
C = []
for _ in range(N):
  X, Y = (int(x) for x in input().split())
  C.append((X,Y))

dp = make_array(2**N, K+1)
d = make_array(2**N)

for i in range(1<<N):
  mx = 0 
  arr = []
  for j in range(N):
    if (i >> j) & 1 == 1:
      arr.append(j)

  for j in range(len(arr)):
    for k in range(j+1,len(arr)):
      val = (C[arr[j]][0] - C[arr[k]][0]) ** 2 + (C[arr[j]][1] - C[arr[k]][1]) ** 2
      mx = max(mx, val)

  d[i] = mx

for i in range(1<<N):
  for j in range(1,K+1):
    k = i
    while k != 0:
      mx = max(dp[k][j-1], d[i-k])
      dp[i][j] = min(dp[i][j], mx)
      k = (k-1) & i

print(dp[1<<N-1][K])

