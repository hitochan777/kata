def getRunLength(s: str):
  cnt = 1
  res = []
  for i in range(1, len(s)):
    if s[i] == s[i-1]:
      cnt += 1
    else:
      res.append((s[i-1], cnt))
      cnt = 1

  res.append((s[-1], cnt))
  return res

N, K = (int(x) for x in input().split())
S = input()
cnt = 0
length = 0
l = 0
ans = 0
T = getRunLength(S)
for r in range(len(T)):
  length += T[r][1]
  if T[r][0] == "0":
    cnt += 1

  while K < cnt:
    length -= T[l][1]
    if T[l][0] == "0":
      cnt -= 1

    l += 1

  ans = max(ans, length)

print(ans)