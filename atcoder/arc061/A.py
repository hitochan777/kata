S = input()
N = len(S)
total = 0
for i in range(1 << (N - 1)):
  cur = S[0]
  for j in range(N-1):
    if (i >> j) & 1 == 1:
      total += int(cur)
      cur = S[j+1]
    else:
      cur += S[j+1]

  total += int(cur)

print(total)