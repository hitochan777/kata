N = int(input())
while N % 2 == 0:
  N //= 2

i = 1
ans = 0
while i**2 <= N:
  if N % i == 0:
    ans += 2
    if i == N // i:
      ans -= 1

  i += 2

print(ans*2)