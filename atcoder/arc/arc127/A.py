N = int(input())

prefix = 1
ans = 0
for i in range(16):
  for j in range(16):
    if N >= (prefix + 1) * (10**j):
      delta = (prefix + 1) * (10**j) - prefix * (10**j)
    elif prefix * (10**j) <= N < (prefix + 1) * (10**j):
      delta = N - prefix * (10**j) + 1
    else:
      delta = 0

    ans += max(delta, 0)

  prefix = prefix * 10 + 1

print(ans)