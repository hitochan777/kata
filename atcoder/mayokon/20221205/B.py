from collections import defaultdict
N, M = (int(x) for x in input().split())
A = []
for _ in range(2*N):
  A.append(input())

def win(a, b):
  if a == "G" and b == "C":
    return True

  if a == "C" and b == "P":
    return True

  if a == "P" and b == "G":
    return True

  return False

rank = list(range(N*2))
wins = {i: 0 for i in range(2*N)}
for i in range(M):
  for j in range(N):
    if win(A[rank[j*2]][i], A[rank[j*2+1]][i]):
      wins[rank[j*2]] += 1
    elif win(A[rank[j*2+1]][i], A[rank[j*2]][i]):
      wins[rank[j*2+1]] += 1

  s = sorted([(-v, k) for k, v in wins.items()])
  for i, (_, k) in enumerate(s):
    rank[i] = k

for i in rank:
  print(i+1)



