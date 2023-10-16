N = int(input())
li = []
total = 0
for _ in range(N):
  A, B = (int(x) for x in input().split())
  li.append((A, B))
  total += A / B

center = total / 2
pos = 0
for A, B in li:
  diff = min(center, A / B)
  pos += diff * B
  center -= diff

print(pos)

  

