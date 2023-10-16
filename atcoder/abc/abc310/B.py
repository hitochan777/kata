N, M = (int(x) for x in input().split())
P = []
C = []
F = []
for _ in range(N):
  p, c, *f = (int(x) for x in input().split())
  P.append(p)
  C.append(c)
  F.append(set(f))

for i in range(N):
  for j in range(N):
    if i == j:
      continue

    if P[i] >= P[j] and F[j].issuperset(F[i]) and (P[i] > P[j] or len(F[j]) > len(F[i])):
      print("Yes")
      exit()

print("No")


  

