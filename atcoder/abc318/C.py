N, D, P = (int(x) for x in input().split())
F = list(int(x) for x in input().split())
F.sort(reverse=True)
cnt = 0
total = 0
ans = 0
for f in F:
  cnt += 1
  total += f
  if cnt == D:
    ans += min(total, P)
    total = 0
    cnt = 0

ans += min(total, P)
print(ans)