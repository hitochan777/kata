N = int(input())
As = []
Bs = []
eaten = set()
for i in range(N):
  A, B = (int(x) for x in input().split())
  As.append((A, i))
  Bs.append((B, i))

As.sort(reverse=True)
Bs.sort(reverse=True)

a = 0
b = 0
asum = 0
bsum = 0
while len(eaten) < N:
  while a < N and As[a][1] in eaten:
    a += 1

  if a < N:
    eaten.add(As[a][1])
    asum += As[a][0]

  while b < N and Bs[b][1] in eaten:
    b += 1

  if b < N:
    eaten.add(Bs[b][1])
    bsum += Bs[b][0]

print(asum - bsum)