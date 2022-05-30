N, M = (int(x) for x in input().split())

lights = []
for _ in range(M):
  k, *s = list(int(x) for x in input().split())
  lights.append(s)

p = list(int(x) for x in input().split())

for i in range(1<<N):
  for j in range(N)
    (i >> j) & 1