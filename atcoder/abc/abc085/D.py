import math

N, H = (int(x) for x in input().split())
weapons = []
max_a = 0
for _ in range(N):
  a, b = (int(x) for x in input().split())
  max_a = max(max_a, a)
  if b > max_a:
    weapons.append(b)

weapons.sort(reverse=True)
p = 0
cnt = 0
while H > 0 and p < len(weapons):
  if weapons[p] < max_a:
    break

  H -= weapons[p]
  cnt += 1
  p += 1

cnt += math.ceil(max(0, H) / max_a)
print(cnt)
