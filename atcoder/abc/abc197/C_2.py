N = int(input())
A = list(int(x) for x in input().split())

ans = 0
for i in range(1<<(N-1)):
  xored = 0
  ored = A[0]
  for j in range(N-1):
    if (i >> j) & 1 == 1:
      ored |= A[j+1]
    else:
      xored ^= ored
      ored = 0

  ans = min(ans, xored)

print(ans)
