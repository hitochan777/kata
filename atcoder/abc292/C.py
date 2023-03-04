def solve(X):
  A = 1
  cnt = 0
  while A**2 < X:
    if X % A == 0:
      cnt += 1

    A += 1

  cnt *= 2
  if A**2 == X:
    cnt += 1
  
  return cnt

N = int(input())
cnt = 0
for Y in range(1, N):
  X = N-Y
  cnt += solve(X) * solve(Y)

print(cnt)