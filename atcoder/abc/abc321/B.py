N, X = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
for i in range(0, 101):
  B = A[:]
  B.append(i)
  B.sort()
  if X <= sum(B[1:-1]):
    print(i)
    exit()

print(-1)
  
