N = int(input())
cnt = 0
for a in range(1, 10**6+1):
  for b in range(a, 10**6+1):
    c = N-a*b
    if c <= 0:
      break

    if a == b:
      cnt += 1
    else:
      cnt += 2

print(cnt)
