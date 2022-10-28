N = int(input())
cards = []
for _ in range(N):
  A, B = (int(x) for x in input().split())
  cards.append((A, B))

ans = 0
for head in range(2):
  for tail in range(2):
    total = 0
    for a, b in cards:
      s = a * ((-1)**head) + b * ((-1)**tail)
      if s > 0:
        total += s

    ans = max(ans, total) 

print(ans)
