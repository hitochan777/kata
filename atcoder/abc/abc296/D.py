import math
N, M = (int(x) for x in input().split())
if N ** 2 < M:
    print(-1)
    exit()

# X = a * b >= M
ans = 10**18
a = 1
while a**2 <= 10**12:
  if a > N:
    break

  b = math.ceil(M / a)
  if b <= N:
    ans = min(ans, a * b)

  a += 1

print(ans)