N, K = (int(x) for x in input().split())
A = list(int(x) for x in input().split())

As = [[] for _ in range(K)]
for i, a in enumerate(A):
  As[i%K].append(a)

for i in range(K):
  As[i].sort()

prev = 0
for i in range(len(As[0])):
  for k in range(K):
    if len(As[k]) <= i:
      continue

    if prev > As[k][i]:
      print("No")
      exit()

    prev = As[k][i]

print("Yes")