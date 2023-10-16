X, Y = (int(x) for x in input().split("."))
X = str(X)
if Y >= 0 and Y <= 2:
  print(X + "-")
elif Y >= 3 and Y <= 6:
  print(X)
else:
  print(X + "+")
