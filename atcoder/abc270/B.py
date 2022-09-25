X, Y, Z = (int(x) for x in input().split())

if X * Y < 0:
  print(abs(X))
  exit()

if X < 0:
  X *= -1
  Y *= -1
  Z *= -1

if X < Y:
  print(X)
  exit()

if Y < Z:
  print(-1)
  exit()

if Z > 0:
  print(X)
  exit()

print(abs(Z) * 2 + X)