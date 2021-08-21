import random
N = 2000

print(N)
for _ in range(N):
  x, y = random.randint(0, 10**9), random.randint(0, 10**9)
  print(x, y)
