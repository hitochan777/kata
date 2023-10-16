N, M, T = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
bonus = {}
for _ in range(M):
  X, Y = (int(x) for x in input().split())
  bonus[X-1] = Y

i = 0
while i < N -1 and T > 0:
  T -= A[i]
  if T <= 0:
    break

  i += 1
  if i in bonus:
    T += bonus[i]

if T > 0 and i == N - 1:
  print("Yes")
else:
  print("No")