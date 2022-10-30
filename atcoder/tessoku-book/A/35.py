N = int(input())
A = list(int(x) for x in input().split())

for i in range(N, 1, -1):
  newA = []
  fn = min if i % 2 != 0 else max
  for j in range(len(A)-1):
    newA.append(fn(A[j], A[j+1]))

  A = newA

print(A[0])
