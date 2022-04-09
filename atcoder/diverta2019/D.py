N = int(input())
m = 1
ans = 0
while m ** 2 <= N:
  if N % m != 0:
    m += 1
    continue

  r = m-1
  if r > 0 and N // r == N % r:
    ans += r

  r = N//m-1
  if r > 0 and N // r == N % r:
    ans += r

  m += 1

print(ans)