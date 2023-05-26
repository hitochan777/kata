N, M = (int(x) for x in input().split())
A = list(int(x)-1 for x in input().split())
B = list(range(N))
C = B.copy()
pos = [0] * N
for a in A:
  C[a], C[a+1] = C[a+1], C[a]

for i, c in enumerate(C):
  pos[c] = i

for a in A:
  if B[a] == 0:
    print(pos[B[a+1]]+1)
  elif B[a+1] == 0:
    print(pos[B[a]]+1)
  else:
    print(pos[0]+1)
    
  B[a], B[a+1] = B[a+1], B[a]

