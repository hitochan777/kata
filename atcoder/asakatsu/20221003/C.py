N, K, S = (int(x) for x in input().split())

ans = [S] * K
for i in range(N-K):
  ans.append(1 if S == 10**9 else 10**9)

print(*ans)