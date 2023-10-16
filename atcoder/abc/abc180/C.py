n = int(input())

i = 1
former = []
while i * i <= n:
  if n % i == 0:
    print(i)
    if i * i != n:
      former.append(i)

  i += 1

for i in former[::-1]:
  print(n // i)
