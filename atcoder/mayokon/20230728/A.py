r, D, x = (int(x) for x in input().split())
for i in range(10):
  x = r * x - D
  print(x)
