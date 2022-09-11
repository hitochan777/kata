N = int(input())
P = list(int(x) for x in input().split())

scores = [0] * N
for i, p in enumerate(P):
  scores[(p-i+N) % N] += 1
  scores[(p-i-1+N) % N] += 1
  scores[(p-i+1+N) % N] += 1

print(max(scores))

