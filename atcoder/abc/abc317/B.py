N = int(input())
A = set(list(int(x) for x in input().split()))
for i in range(1, 1001):
  exists = 0
  for j in range(i, i + N + 1):
    if j in A:
      exists += 1

  if exists == N:
    for j in range(i, i + N + 1):
      if j not in A:
        print(j)
        exit()
