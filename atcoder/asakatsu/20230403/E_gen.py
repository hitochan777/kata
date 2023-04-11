import random
import numpy as np

N = random.randint(1, 10)
K = random.randint(1, 10)
P = [x + 1 for x in np.random.permutation(N)]
C = []
for _ in range(N):
    C.append(random.randint(1, 10))

print(N, K)
print(*P)
print(*C)
