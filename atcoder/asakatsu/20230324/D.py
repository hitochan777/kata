N = int(input())
S = list(input())
T = list(input())
idx = [i for i, c in enumerate(S) if c == "1"]
p = 0
ans = 0
# print(idx)
for i in range(N):
  s, t = S[i], T[i]
  # print(s,t)
  if s == t:
      continue

  while p < len(idx) and idx[p] <= i:
    p += 1

  if p >= len(idx):
      print(-1)
      exit()

  S[idx[p]] = "0"
  ans += idx[p] - i
  p += 1
  # print(ans, S, T)

print(ans)