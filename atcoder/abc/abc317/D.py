INF = 10**18
def minimum_cost(items, X):
    n = len(items)
    dp = [[INF] * (X + 1) for _ in range(n + 1)]
    for i in range(n+1):
       dp[i][0] = 0
    
    for i in range(1, n + 1):
        ci, vi = items[i - 1]
        
        for v in range(X + 1):
            # print(i, v, vi, dp[i, v])
            dp[i][v] = dp[i - 1][v]
            
            dp[i][v] = min(dp[i][v], dp[i - 1][max(0, v - vi)] + ci)
    
    # print(dp)
    min_cost = min(dp[n][X:])
    return min_cost

N = int(input())
T = 0 
sub = 0
items = []
for _ in range(N):
  X, Y, Z = (int(x) for x in input().split())
  if X > Y:
    sub += Z
  else:
     items.append(((Y - X + 1)//2, Z))

  T += Z

T = max(0, (T + 1) // 2 - sub)
# print(T, items)
ans = minimum_cost(items, T)
print(ans)