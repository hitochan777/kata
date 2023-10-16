from itertools import permutations

def is_gakkari(orders):
  for i in range(3):
    vals = []
    for j in range(3):
      vals.append((orders[(i, j)], g[i][j]))

    vals.sort()
    if vals[0][1] == vals[1][1] and vals[2][1] != vals[0][1]:
      return True

  for j in range(3):
    vals = []
    for i in range(3):
      vals.append((orders[(i, j)], g[i][j]))

    vals.sort()
    if vals[0][1] == vals[1][1] and vals[2][1] != vals[0][1]:
      return True

  vals = []
  for i in range(3):
    vals.append((orders[(i, i)], g[i][i]))

  vals.sort()
  if vals[0][1] == vals[1][1] and vals[2][1] != vals[0][1]:
    return True

  vals = []
  for i in range(3):
    vals.append((orders[(i, 2-i)], g[i][2-i]))

  vals.sort()
  if vals[0][1] == vals[1][1] and vals[2][1] != vals[0][1]:
    return True

  return False
  

g = []
for _ in range(3):
  c = list(int(x) for x in input().split())
  g.append(c)

cnt = 0
gakkari = 0
for p in permutations(range(9)):
  orders = {}
  for i, val in enumerate(p):
    x = val // 3
    y = val % 3
    orders[(x,y)] = i

  cnt += 1
  if is_gakkari(orders):
    gakkari += 1

# print(cnt)
print((cnt-gakkari)/cnt)

