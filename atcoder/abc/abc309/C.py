N, K = (int(x) for x in input().split())
doses = []
for _ in range(N):
  a, b = (int(x) for x in input().split())
  doses.append((a,b))

bad, good = 0, 10**10
while good - bad > 1:
  m = (good + bad) >> 1
  total = sum(b for a, b in doses if m <= a)
  if total <= K:
    good = m
  else:
    bad = m

print(good)
