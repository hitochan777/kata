N = int(input())

s = set()
cur = 6
while cur <= 10000:
  s.add(cur)
  cur += 6

cur = 10
while cur <= 10000:
  s.add(cur)
  cur += 10

cur = 15
while cur <= 10000:
  s.add(cur)
  cur += 15

ans = sorted(list(s))[:N]
ans[2], ans[3] = ans[3], ans[2]
print(*ans)