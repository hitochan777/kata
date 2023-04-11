N, K = (int(x) for x in input().split())
P = list(int(x)-1 for x in input().split())
C = list(int(x) for x in input().split())

ans = -10**18
for i in range(N):
  for k in range(1,K+1):
    cur = i
    total = 0
    for _ in range(k):
      total += C[P[cur]]
      cur = P[cur]

    ans = max(total, ans)

print(ans)