A, B, C, D, E, F, X = (int(x) for x in input().split())
tlocs = []
cur = 0
alocs = []
while len(tlocs) < X:
  for i in range(A):
    cur += B
    tlocs.append(cur)

  for i in range(C):
    tlocs.append(cur)

cur = 0
while len(alocs) < X:
  for i in range(D):
    cur += E
    alocs.append(cur)

  for i in range(F):
    alocs.append(cur)

if tlocs[X-1] > alocs[X-1]:
  print("Takahashi")
elif tlocs[X-1] < alocs[X-1]:
  print("Aoki")
else:
  print("Draw")