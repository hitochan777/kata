N, M = (int(x) for x in input().split())
count = {i: 0 for i in range(2 * N)}

A = []
rank = list(range(2 * N))
for _ in range(2 * N):
  a = list(input())
  A.append(a)

for i in range(M):
  for j in range(0, 2 * N, 2):
    p1, p2 = rank[j], rank[j+1]
    a, b = A[p1][i], A[p2][i]
    winner = None
    if a == "G" and b == "C":
      winner = p1
    elif a == "C" and b == "G":
      winner = p2
    elif a == "C" and b == "P":
      winner = p1
    elif a == "P" and b == "C":
      winner = p2
    elif a == "P" and b == "G":
      winner = p1
    elif a == "G" and b == "P":
      winner = p2

    if winner is not None:
      count[winner] -= 1

  st = sorted((cnt, num) for num, cnt in count.items())
  rank = list(map(lambda v: v[1], st))

for i in range(2 * N):
  print(rank[i]+1)


