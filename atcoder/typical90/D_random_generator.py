import random
H, W = random.randint(1, 2000), random.randint(1, 2000)
print(H, W)
for _ in range(H):
  for _ in range(W):
    print(random.randint(1, 99), end=" ")

  print("")