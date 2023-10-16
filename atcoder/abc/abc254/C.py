N, K = (int(x) for x in input().split())
A = list(int(x) for x in input().split())

lili = []
for i in range(K):
  li = []
  for j in range(i, N, K):
    li.append(A[j]) 

  li.sort()
  lili.append(li)

prev = 1
for i in range(len(lili[0])):
  for j in range(len(lili)):
    if len(lili[j]) <= i:
      break

    if lili[j][i] < prev:
      print("No")
      exit()

    prev = lili[j][i]

print("Yes")