X, Y = (int(x) for x in input().split())
ops = [(X,Y)]
while (X, Y) != (1, 1):
  if X > Y:
    X, Y = X-Y, Y
  else:
    X, Y = X, Y-X

  ops.append((X,Y))

ops = ops[:-1]
print(len(ops))
for op in ops[::-1]:
  print(*op)