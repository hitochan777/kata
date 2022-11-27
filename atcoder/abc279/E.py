N, M = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
B = list(range(N+1))

for a in A:
  B[a], B[a+1] = B[a+1], B[a]

pos = {}
for i, b in enumerate(B):
  pos[b] = i

B = list(range(N+1))
for a in A:
  if B[a] == 1:
    print(pos[B[a+1]])
  elif B[a+1] == 1:
    print(pos[B[a]])
  else:
    print(pos[1])

  B[a], B[a+1] = B[a+1], B[a]

