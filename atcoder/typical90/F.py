N, K = (int(x) for x in input().split())
S = input()

c = [[None] * 26 for _ in range(N)]

for i in range(N-1, -1, -1):
  for j in range(26):
    c[i][j] = None

ans = ""
for i in range(K):
  for j in range(26):
    next_pos = c[i][j]
    length = N - next_pos + i
    if length >= K:
      ans += chr(ord('a') + j)

print(ans)
      