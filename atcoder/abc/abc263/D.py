N, L, R = (int(x) for x in input().split())
A = list(int(x) for x in input().split())

f, g = [0], [0]
for i, a in enumerate(A):
  f.append(min(f[-1] + a, L*(i+1)))

for i, a in enumerate(A[::-1]):
  g.append(min(g[-1] + a, R*(i+1)))

ans = 10**18
for i in range(N+1):
  ans = min(f[i] + g[N-i], ans)

print(ans)