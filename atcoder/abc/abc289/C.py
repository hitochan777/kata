def satisfy(sets, N):
  return all(any(x in s for s in sets) for x in range(1, N+1))

N, M = (int(x) for x in input().split())
sets = []
for _ in range(M):
  C = int(input())
  s = set(int(x) for x in input().split())
  sets.append(s)

cnt = 0
for i in range(1<<M):
  parts = []
  for j in range(M):
    if (i >> j) & 1 == 1:
      parts.append(sets[j])

  if satisfy(parts, N):
    cnt += 1

print(cnt)
