N, M = (int(x) for x in input().split())

A = []
for _ in range(N):
  A.append(list(input()))

B = []
for _ in range(M):
  B.append(list(input()))

for i in range(N-M+1):
  for j in range(N-M+1):
    if all(A[i+k][j+l] == B[k][l] for k in range(M) for l in range(M)):
      print("Yes")
      exit()

print("No")
        