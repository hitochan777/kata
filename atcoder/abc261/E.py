N, C = (int(x) for x in input().split())
ops = []
for _ in range(N):
  T, A = (int(x) for x in input().split())
  ops.append((T, A))

zeros = [0]
ones = [(1<<32)-1]
for T, A in ops:
  if T == 1:
    zeros.append(zeros[-1] & A)
    ones.append(ones[-1] & A)
  elif T == 2:
    zeros.append(zeros[-1] | A)
    ones.append(ones[-1] | A)
  else:
    zeros.append(zeros[-1] ^ A)
    ones.append(ones[-1] ^ A)

X = C
for i in range(N):
  zero, one = zeros[i+1], ones[i+1]
  newX = 0
  for j in range(32):
    if (X >> j) & 1 == 1:
      newX |= ((one >> j) & 1) << j
    else:
      newX |= ((zero >> j) & 1) << j
      
  print(newX)
  X = newX



