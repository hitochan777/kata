N, K = (int(x) for x in input().split())
S = input()

c = [[K] * 26 for _ in range(N+1)]

for i in range(26):
  c[N][i] = N

for i in range(N-1, -1, -1):
  for j in range(26):
    if S[i] == chr(ord('a') + j):
      c[i][j] = i
    else:
      c[i][j] = c[i+1][j]

ans = ""
cur_pos = 0
for i in range(K):
  for j in range(26):
    next_pos = c[cur_pos][j]
    length = N - next_pos + i
    if length >= K:
      ans += chr(ord('a') + j)
      cur_pos = next_pos + 1
      break

print(ans)