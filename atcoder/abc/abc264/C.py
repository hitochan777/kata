H1, W1 = (int(x) for x in input().split())
A = [] 
for _ in range(H1):
  row = list(int(x) for x in input().split())
  A.append(row)

H2, W2 = (int(x) for x in input().split())
B = [] 
for _ in range(H2):
  row = list(int(x) for x in input().split())
  B.append(row)

for i in range(1<<(H1+W1)):
  rows = set()
  cols = set()
  for j in range(H1+W1):
    if (i >> j) & 1 == 0:
      continue

    if j < H1:
      rows.add(j)
    else:
      cols.add(j - H1)

  new_mat = []
  for k in range(H1):
    r = []
    if k in rows:
      continue
    for l in range(W1):
      if l in cols:
        continue

      r.append(A[k][l])
    
    if len(r) > 0:
      new_mat.append(r)

  # print(len(new_mat), len(B),len(new_mat[0]),len(B[0]), rows)
  if len(new_mat) == len(B) and len(new_mat[0]) == len(B[0]):
    if all(new_mat[k][l] == B[k][l] for k in range(len(new_mat)) for l in range(len(new_mat[0]))):
      print("Yes")
      exit()

print("No")