s = input()
p, q = 0, len(s)-1
ans = 0
while p < q:
  if s[p] == s[q]:
    p, q = p + 1, q - 1
    continue

  if s[p] == "x":
    p += 1
    ans += 1
    continue

  if s[q] == "x":
    q -= 1
    ans += 1
    continue

  print(-1)
  exit()

print(ans)