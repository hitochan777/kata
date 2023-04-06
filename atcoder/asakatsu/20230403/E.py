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
      acc.append(acc[0] + score)

  accs.append(acc) 



