N = int(input())
hints = []
for _ in range(N):
  hints.append(list(int(x) for x in input().split()))

for Cx in range(101):
  for Cy in range(101):
    hs = set()
    min_val = 10**18
    for x, y, h in hints:
      diff = abs(x-Cx) + abs(y-Cy)
      if h > 0:
        hs.add(diff + h)
      else:
        min_val = min(min_val, diff)

    if len(hs) == 1:
      H = hs.pop()
      if H <= min_val:
        print(Cx, Cy, H)
        exit()