H, W, A, B = (int(x) for x in input().split())

for i in range(H):
  for j in range(W):
    if i < B and j < A:
      print(0, end="")
    elif i < B or j < A:
      print(1, end="")
    else:
      print("0", end="")

  print()