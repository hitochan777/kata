import random

maxN = 3

N = random.randint(1, maxN)
M = random.randint(N-1, N*(N-1)//2)
print(N, M)
edges = set()
for _ in range(M):
  while True:
    a = random.randint(1, N-1)
    b = random.randint(a+1, N)
    if (a, b) not in edges:
      edges.add((a, b))
      break

for a, b in edges:
  print(a, b)

K = random.randint(0, N)
print(K)
li = list(x + 1 for x in range(N))
P = random.sample(li, K)
D = []
for _ in range(K):
  D.append(random.randint(0, N))

for p, d in zip(P, D):
  print(p, d)


