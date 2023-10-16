N, A, B = (int(x) for x in input().split())
for i in range(N * A):
  row = []
  for j in range(N * B):
    if ((i // A) + (j // B)) % 2 == 0:
      row.append(".")
    else:
      row.append("#")

  print("".join(row))