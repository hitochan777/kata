N = int(input())
table = []
for _ in range(N):
  table.append(input())

for i in range(N):
  for j in range(i):
    if table[i][j] == "W" and table[j][i] != "L":
      print("incorrect")
      exit()

    if table[i][j] == "L" and table[j][i] != "W":
      print("incorrect")
      exit()

    if table[i][j] == "D" and table[j][i] != "D":
      print("incorrect")
      exit()

print("correct")