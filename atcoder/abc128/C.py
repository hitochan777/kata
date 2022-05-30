N, M = (int(x) for x in input().split())

lights = []
for _ in range(M):
  k, *s = list(int(x)-1 for x in input().split())
  lights.append(s)

p = list(int(x) for x in input().split())

ans = 0
for i in range(1<<N):
  on_nums = set(j for j in range(N) if (i >> j) & 1 == 1)
  total = 0
  for j, light in enumerate(lights):
    cnt = sum(1 for switch in light if switch in on_nums)
    if cnt % 2 == p[j]:
      total += 1
    
  if total == M:
    ans += 1

print(ans)