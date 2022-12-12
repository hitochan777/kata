N = int(input())
digits = []
for i in range(61):
  if (N >> i) & 1 == 1:
    digits.append(i)

M = len(digits)
ans = []
for i in range(1<<M):
  val = 0
  for j in range(M):
    if (i >> j) & 1 == 1:
      val += 1 << digits[j]

  ans.append(val)

ans.sort()
for v in ans:
  print(v)