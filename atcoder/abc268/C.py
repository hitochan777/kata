N = int(input())
P = list(int(x) for x in input().split())

ans = 0
for i in range(100):
  s = sum(1 for j in range(N) if (P[j] + i) % N in [(j+1) % N, j, (j-1+N) % N])
  # print(i, s)
  ans = max(s, ans)

print(ans)

