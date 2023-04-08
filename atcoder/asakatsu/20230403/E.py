N, K = (int(x) for x in input().split())
P = list(int(x)-1 for x in input().split())
C = list(int(x) for x in input().split())

accs = []
visited = set()
for i in range(N):
  if i in visited:
    continue

  scores = []
  cur = i
  while cur not in visited:
    scores.append(C[cur])
    visited.add(cur)
    cur = P[cur]

  acc = [0]
  for i in range(2):
    for score in scores:
      acc.append(acc[-1] + score)

  accs.append(acc) 

# print(accs)
ans = -10**18
for acc in accs:
  M = (len(acc) - 1) >> 1
  # print(M)
  for r in range(min(M+1, K+1)):
    for i in range(M):
      val = acc[i+r] - acc[i]
      if r == 0:
        if K - r // M == 0 or acc[M] < 0:
          continue

      ans = max(ans, val + max(0, acc[M]) * (K - r) // M)
      
print(ans)