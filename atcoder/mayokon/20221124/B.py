N = int(input())
A = list(int(x) for x in input().split())

cnt = [0] * N
for i, a in enumerate(A):
  cnt[a-1] += 1

for c in cnt:
  print(c)