N = int(input())
P = list(int(x) for x in input().split())
li = [None] * N

for i, p in enumerate(P):
  li[p-1] = i + 1

print(" ".join([str(x) for x in li]))