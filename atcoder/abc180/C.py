n = int(input())

i = 1
cnt = 0
while i * i <= n:
  if n % i == 0:
    cnt += 1

  i += 1

print(cnt)
