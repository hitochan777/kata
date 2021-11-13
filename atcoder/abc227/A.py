N, K, A = (int(x) for x in input().split())
n = 0
for i in range(K):
  n = (A - 1 + i) % N

print(n+1)