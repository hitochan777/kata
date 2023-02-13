N = int(input())

ans = 10**18
a = 1
while a**2 <= N:
  if N % a != 0:
    a += 1
    continue

  b = N // a
  ans = min(ans, max(len(str(a)), len(str(b))))
  a += 1

print(ans)