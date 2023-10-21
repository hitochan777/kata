N = int(input())
places = []
for _ in range(N):
  W, X = (int(x) for x in input().split())
  places.append((W, X))

ans = 0
for t in range(24):
  val = 0
  for w, x in places:
    if 9 <= (t + x) % 24 <= 17:
      val += w

  ans = max(ans, val)

print(ans)
  