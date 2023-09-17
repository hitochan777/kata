M = int(input())
S = []
for _ in range(3):
  s = input()
  S.append(s*3)

INF = 10**5
ans = INF
for i in range(10):
  c = str(i)
  if any(c not in s for s in S):
    continue

  used = set()
  for s in S:
    start = 0
    while True:
      index = s.find(c, start)
      assert index >= 0
      if index not in used:
        used.add(index)
        break

      start = index+1

  ans = min(ans, max(used))

if ans == INF:
  print(-1)
else:
  print(ans)