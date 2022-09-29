N = int(input())

i = 1
s = set()
while i * i <= N:
  if N % i == 0:
    s.add(i)
    s.add(N//i)

  i += 1

for v in sorted(list(s)):
  print(v)