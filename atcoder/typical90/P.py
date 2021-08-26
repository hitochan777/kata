N = int(input())
A, B, C = (int(x) for x in input().split())

min_val = 10000
for a in range(10000):
  for b in range(10000-a):
    tmp = N - (A * a + B * b)
    if tmp < 0:
      continue

    if tmp % C == 0:
      min_val = min(a + b + tmp // C, min_val)

print(min_val)
