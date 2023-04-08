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
  for r in range(min(M, K+1)):
    for i in range(M):
      val = acc[i+r] - acc[i]
      q = (K - r) // M
      if r == 0 and q == 0:
          continue

      if acc[M] > 0:
        ans = max(ans, val + acc[M] * q)
      elif r > 0:
        ans = max(ans, val)
      
print(ans)