N = int(input())
A = []
for _ in range(N):
  a = int(input())
  A.append(a)

def solve(A):
  if A[0] != 0:
    return False

  if all(abs(A[i+1] - A[i]) == 1 for i in range(N-1)):
    return (True,  sum(1 for a in range(A) if a != 0))
  else:
    (False, 0)

ok, cnt = solve(A)
if ok:
  print(cnt)
else:
  print(-1)