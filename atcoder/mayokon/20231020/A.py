N, X, Y, Z = (int(x) for x in input().split())
A = list((int(x), -i) for i, x in enumerate(input().split()))
B = list((int(x), -i) for i, x in enumerate(input().split()))
C = list((a + b, -i) for i, ((a, _), (b, _)) in enumerate(zip(A, B)))

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

passed = set()
for i in range(X):
  passed.add(A[i][1])

cnt = 0
i = 0 
while cnt < Y:
  if B[i][1] not in passed:
    passed.add(B[i][1])
    cnt += 1
  
  i += 1


cnt = 0
i = 0 
while cnt < Z:
  if C[i][1] not in passed:
    passed.add(C[i][1])
    cnt += 1

  i += 1


ans = sorted(-i+ 1 for i in passed)
print(*ans)

