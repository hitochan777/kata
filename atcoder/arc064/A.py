N, x = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
newA = [min(x, A[0])]

for i in range(1, N):
  newA.append(min(A[i], max(x-newA[-1], 0)))

print(sum(max(a - b, 0) for a, b in zip(A, newA)))
