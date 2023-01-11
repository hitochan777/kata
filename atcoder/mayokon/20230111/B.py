N, K = (int(x) for x in input().split())
H = []
for _ in range(N):
  h = int(input())
  H.append(h)

H.sort()
ans = 10**18
for i in range(N-K+1):
  ans = min(ans, H[i+K-1] - H[i])

print(ans)