import random
H, W = 2000, 2000
print(H, W)
for _ in range(H):
  for _ in range(W):
    print(random.randint(1, 99), end=" ")