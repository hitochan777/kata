N, K = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
l, h = 0, 10**18
while h - l > 1:
  m = (l+h) >> 1
  total = sum(min(a, m) for a in A)
  if total >= K * m:
    l = m
  else:
    h = m

print(l)


