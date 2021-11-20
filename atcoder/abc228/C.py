N, K = (int(x) for x in input().split())
sums = []
for i in range(N):
  sums.append(((sum(int(x) for x in input().split())), i))


possibles = [False] * N
sums.sort()
for i in range(N):
  if sums[-K][0] - sums[i][0] <= 300:
    possibles[sums[i][1]] = True

for possible in possibles:
  print("Yes" if possible else "No")

