A, B, X = (int(x) for x in input().split())

ok, ng = 0, 10**9+1

while ng - ok > 1:
  n = (ng + ok) >> 1
  if X >= A * n + B * len(str(n)):
    ok = n
  else:
    ng = n

print(ok)