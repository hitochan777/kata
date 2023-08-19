import numpy as np

H, W = 2000, 2000
random_colors = np.random.choice(list("ab"), size=(H, W))

print(H, W)
for i in range(H):
    print("".join(random_colors[i]))