N, X = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
cost = 0
for i, a in enumerate(A):
  if i % 2 == 0:
    cost += a
  else:
    cost += a - 1

if cost <= X:
  print("Yes")
else:
  print("No")