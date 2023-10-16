N = int(input())
s = list(input())
cnt = [[10**6] * 26 for _ in range(N)]
for i in range(N):
  if i > 0:
    for j in range(26):
      cnt[i][j] = cnt[i-1][j]

  ch = ord(s[i]) - ord("a")
  cnt[i][ch] = i

p, q = 0, N-1
while p < q:
  for ch in range(ord(s[p])-ord("a")):
    if p < cnt[q][ch] <= q:
      q = cnt[q][ch]
      s[p], s[q] = s[q], s[p]
      q -= 1
      break

  p += 1

print("".join(s))